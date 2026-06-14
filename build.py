#!/usr/bin/env python3
"""Quipu-Log 교과서 빌드 (이중 언어).

- 영문(en)을 루트에 생성(기본 노출): index.html, NN-slug.html
- 한글(ko)을 ko/ 에 생성: ko/index.html, ko/NN-slug.html
- 본문 조각: bodies/<lang>/NN-slug.html (있으면 사용, 없으면 '준비중')
- 공용 에셋: assets/ (루트). ko/ 페이지는 ../assets/ 로 링크.
- 각 페이지 상단에 EN/KO 언어 토글 + 좌측 목차 + 하단 이전/다음.
사용법: python3 build.py
"""
import json, os, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
M = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))

# 언어별 설정: outdir(루트 기준), 에셋 접두사, 다른 언어 페이지 접두사(상호 토글)
LANGS = {
    "en": {"outdir": ".",  "assets": "assets/",    "other": "ko", "other_prefix": "ko/"},
    "ko": {"outdir": "ko", "assets": "../assets/", "other": "en", "other_prefix": "../"},
}
T = {  # UI 문자열
    "en": {"prev": "Prev", "next": "Next", "contents": "Contents", "cover": "Cover",
           "coming": "Coming soon", "coming_body": "This chapter hasn’t been written yet.",
           "herotitle": "Tamper-evident audit logs<br>and a filesystem storage engine",
           "herolead": " — build intuition from analogies, confirm against real code, and see how database-grade guarantees are rebuilt on nothing but plain files."},
    "ko": {"prev": "이전", "next": "다음", "contents": "목차", "cover": "표지로",
           "coming": "준비중", "coming_body": "이 챕터는 아직 집필되지 않았습니다.",
           "herotitle": "변조-탐지 감사 로그와<br>파일시스템 저장 엔진",
           "herolead": ". 비유로 직관을 잡고, 실제 코드로 확인하며, DB가 주던 보장이 파일 위에서 어떻게 다시 만들어지는지 짚어갑니다."},
}

def title(M, lang): return M[f"title_{lang}"]
def subtitle(M, lang): return M[f"subtitle_{lang}"]
def ptitle(ch, lang): return ch[f"title_{lang}"]

def chapters():
    out=[]
    for p in M["parts"]:
        for c in p["chapters"]:
            out.append({**c, "part_en": p["name_en"], "part_ko": p["name_ko"]})
    return out

def page_file(c): return f'{c["n"]}-{c["slug"]}.html'

def nav_html(lang, active_n):
    cfg=LANGS[lang]; o=[]
    o.append('<nav class="toc" id="toc">')
    # 언어 토글
    en_cls = "langbtn active" if lang=="en" else "langbtn"
    ko_cls = "langbtn active" if lang=="ko" else "langbtn"
    if active_n:
        cur=page_file(next(c for c in chapters() if c["n"]==active_n))
        en_href = cur if lang=="en" else f"../{cur}"
        ko_href = f"ko/{cur}" if lang=="en" else cur
    else:
        en_href = "index.html" if lang=="en" else "../index.html"
        ko_href = "ko/index.html" if lang=="en" else "index.html"
    o.append(f'<div class="langtoggle"><a class="{en_cls}" href="{en_href}">EN</a>'
             f'<a class="{ko_cls}" href="{ko_href}">한국어</a></div>')
    o.append(f'<a class="home" href="index.html">{html.escape(title(M,lang))}</a>')
    o.append(f'<div class="sub">{html.escape(subtitle(M,lang))}</div>')
    for p in M["parts"]:
        o.append(f'<div class="part">{html.escape(p[f"name_{lang}"])}</div>')
        for c in p["chapters"]:
            cls="lnk active" if c["n"]==active_n else "lnk"
            o.append(f'<a class="{cls}" href="{page_file(c)}"><span class="n">{c["n"]}</span>{html.escape(ptitle(c,lang))}</a>')
    o.append('</nav>')
    return "\n".join(o)

def prevnext(lang, idx, chs):
    t=T[lang]
    if idx>0:
        p=chs[idx-1]; prev=f'<a class="prev" href="{page_file(p)}"><span class="dir">← {t["prev"]}</span><span class="t">{p["n"]} · {html.escape(ptitle(p,lang))}</span></a>'
    else:
        prev=f'<a class="prev" href="index.html"><span class="dir">← {t["contents"]}</span><span class="t">{t["cover"]}</span></a>'
    if idx<len(chs)-1:
        nx=chs[idx+1]; nextn=f'<a class="next" href="{page_file(nx)}"><span class="dir">{t["next"]} →</span><span class="t">{nx["n"]} · {html.escape(ptitle(nx,lang))}</span></a>'
    else:
        nextn='<div class="ph"></div>'
    return f'<div class="prevnext">{prev}{nextn}</div>'

def shell(lang, page_title, active_n, content, prevnext_html):
    cfg=LANGS[lang]; A=cfg["assets"]
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page_title)}</title>
<link rel="stylesheet" href="{A}style.css">
</head>
<body>
<div class="topbar"><button id="menuBtn">☰ {T[lang]["contents"]}</button><b>{html.escape(title(M,lang))}</b></div>
<div class="wrap">
{nav_html(lang, active_n)}
<main>
<div class="inner">
{content}
{prevnext_html}
</div>
</main>
</div>
<script src="{A}textbook.js"></script>
</body>
</html>
'''

def build_lang(lang):
    cfg=LANGS[lang]; t=T[lang]
    outdir=ROOT/cfg["outdir"]; outdir.mkdir(parents=True, exist_ok=True)
    bodies=ROOT/"bodies"/lang
    chs=chapters(); built=0; pending=[]
    placeholder=(f'<article><div class="callout warn"><span class="lab">{t["coming"]}</span>'
                 f'<p>{t["coming_body"]}</p></div></article>')
    for idx,c in enumerate(chs):
        bf=bodies/page_file(c)
        if bf.exists() and bf.read_text(encoding="utf-8").strip():
            body=bf.read_text(encoding="utf-8"); built+=1
        else:
            body=placeholder; pending.append(c["n"])
        top=(f'<div class="chaptertop"><span class="partlabel">{html.escape(c[f"part_{lang}"])}</span>'
             f'<h1><span class="chno">{c["n"]}</span> · {html.escape(ptitle(c,lang))}</h1></div>')
        (outdir/page_file(c)).write_text(
            shell(lang, f'{c["n"]} · {ptitle(c,lang)} — {title(M,lang)}', c["n"], top+body, prevnext(lang,idx,chs)),
            encoding="utf-8")
    # 표지
    hero=(f'<header class="hero"><div class="eyebrow">{html.escape(title(M,lang))}</div>'
          f'<h1>{t["herotitle"]}</h1>'
          f'<p>{html.escape(subtitle(M,lang))}{t["herolead"]}</p></header>')
    toc=['<div class="toc-grid">']
    for p in M["parts"]:
        toc.append(f'<div class="toc-part">{html.escape(p[f"name_{lang}"])}</div>')
        for c in p["chapters"]:
            toc.append(f'<a class="toc-item" href="{page_file(c)}"><span class="num">{c["n"]}</span><span class="t">{html.escape(ptitle(c,lang))}</span></a>')
    toc.append('</div>')
    (outdir/"index.html").write_text(shell(lang, title(M,lang), "", hero+"\n".join(toc), ""), encoding="utf-8")
    print(f"[{lang}] 빌드: {len(chs)}챕터 (본문 {built}, 준비중 {len(pending)}) → {cfg['outdir']}/")
    if pending: print(f"   준비중: {', '.join(pending)}")

for lang in ("en","ko"):
    build_lang(lang)
