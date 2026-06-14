# Quipu-Log 교과서 — 집필 가이드 (서브에이전트 필독)

너는 이 교과서의 한 파트를 집필한다. **반드시 이 가이드를 끝까지 읽고, 골드 스탠다드 챕터(`bodies/07-append-only-wal.html`)를 먼저 열어 톤·구조·SVG·코드 스타일을 눈으로 익힌 뒤** 집필을 시작하라.

## 0. 독자와 목표 (가장 중요)
- 독자는 **CS 전반과 DB(쿼리·인덱스·트랜잭션)는 어느 정도 안다. 하지만 파일시스템(fs) 레벨과, "DB가 알아서 해주던 것을 파일 위에서 직접 구현하는 법"은 모른다.**
- 그래서 핵심 교수법은 **"DB에서는 ___, 여기선 파일로 ___"** 다리 놓기다. 아는 것(DB)을 사다리로 모르는 것(fs 구현)에 건너가게 하라. fs/저장엔진 주제(파트 2~4)는 깊게, 독자가 아는 영역(파트 7~8)은 가볍게.
- 진짜 학습 대상은 **개념**이다. Quipu-Log 코드는 "그 개념이 실제로 이렇게 쓰였다"는 **참고자료**다. 개념 설명 → 그다음 코드로 확인.
- 문체: **친절한 교과서.** 독자에게 말 걸듯("~해 봅시다", "기억하세요"), 비유로 직관을 먼저 잡고, 어려운 말은 풀어 쓴다. 거들먹거리지 않는다. 존댓말.

## 1. 무엇을 만드나 — 출력 형식
- 너는 `bodies/<NN>-<slug>.html` 파일을 **하나씩** 쓴다 (배정받은 챕터 수만큼).
- 각 파일은 **`<article> ... </article>` 안쪽 본문만** 담는다. `<!DOCTYPE>`, `<head>`, 사이드바, 챕터 제목(chaptertop), 이전/다음 버튼은 **쓰지 마라** — 빌드 스크립트(`build.py`)가 공용 셸로 감싸준다. 챕터 제목(h1)도 자동 생성되니 본문에 또 넣지 마라.
- 파일명은 `manifest.json`의 `n`·`slug`와 정확히 일치해야 한다. (예: `bodies/08-segments.html`)
- 다 쓰면 끝. 빌드·검증은 메인 세션이 한다. **wiki 파일이나 다른 챕터 파일은 절대 건드리지 마라.**

## 2. 챕터 본문 구조 (07을 그대로 따르라)
1. `<p class="lead">` — 도입 한 문단. 이 챕터에서 무엇을, 왜 배우는지. 호기심 유발.
2. `<div class="callout"><span class="lab">한 문장 요약</span>...</div>` — 핵심을 한 문장으로 (선택이지만 권장).
3. `<h2>` 섹션들 — 보통 이 흐름: **「당신이 아는 것(DB)」 → 「발상/개념」 → 「어떻게(코드로 확인)」 → 「왜 이렇게(트레이드오프)」 → 「정리」**. h2 제목은 딱딱한 "무엇을/왜"가 아니라 말이 되는 제목으로.
4. 본문 중간중간 colored callout (아래 4절), **최소 1개의 SVG 그림**(5절), **핵심이 강조된 코드 스니펫**(6절).
5. 마지막에 `<div class="callout check"><span class="lab">스스로 확인</span>...</div>` — 독자가 답해볼 질문 2~3개.

## 3. 정확성 규칙 (반드시)
- 코드 스니펫·동작 설명은 **실제 소스에서 확인하고 써라.** 소스 루트: `~/Desktop/quipu-log`. 추측·창작 금지. API 이름·필드명은 실제와 일치해야 한다.
- 한글 용어·맥락은 기존 위키 암묵지를 참고하면 일관된다: `~/Desktop/augmentation-note/pages/암묵지___Quipu-Log *.md`.
- 의심스러우면 코드를 `grep`/`read`로 직접 확인하라. 짧게 인용하되, 핵심만.

## 4. CSS 클래스 어휘 (정의된 것만 써라)
- `<p class="lead">` 도입 문단.
- 콜아웃: `<div class="callout TYPE"><span class="lab">라벨</span><p>...</p></div>`
  - `why` — 왜 이렇게 설계했나 (파란색). 라벨 예: "왜 이렇게?"
  - `dbfs` — **DB↔파일시스템 대응** (청록). 라벨: "DB ↔ 파일시스템". fs 챕터에 적극 사용.
  - `analogy` — 비유 (보라). 라벨: "비유"
  - `warn` — 함정·한계 (노랑). 라벨: "주의"
  - `key` — 보안 포인트 (빨강). 라벨: "보안 포인트"
  - `check` — 확인 질문 (초록). 라벨: "스스로 확인". 마지막에.
  - 타입 없는 `callout` — 일반 강조 박스.
- `<span class="pill">15장 인덱싱</span>` — 다른 챕터 상호참조용 알약 뱃지.
- `<table>` — 비교표. DB↔FS 대비, 옵션 비교에 좋다.
- `<figure><svg>...</svg><figcaption>...</figcaption></figure>` — 그림.
- 인라인 코드 `<code>...</code>`, 코드블록 `<pre><code>...</code></pre>`.
- 새 클래스를 발명하지 마라. style.css에 있는 것만 쓴다.

## 5. SVG 그림 규칙 (직관용 — 필수)
- 각 챕터에 **개념을 한눈에 보여주는 인라인 `<svg>` 1개 이상**. 글로 설명하기 어려운 구조·흐름·비교를 그림으로.
- `<figure>` 안에 `<svg viewBox="0 0 W H" role="img" aria-label="설명">`, 끝에 `<figcaption>` 한 줄.
- 다크 테마 팔레트 사용: 배경 `#0b0d12`/`#161922`, 선 `#2a2f3d`, 글자 `#e6e8ee`(밝은)·`#9aa3b2`(흐린), 강조색 파랑 `#7aa2ff`·청록 `#8be9c0`·노랑 `#ffd479`·빨강 `#ff8b8b`·보라 `#c792ea`.
- 폰트는 `-apple-system,sans-serif`. 화살표는 `<marker>`로. 07의 SVG를 복붙해서 변형하는 걸 권장.
- 과하게 화려할 필요 없다. **명료함 > 장식.** 박스+화살표+라벨이면 충분.

## 6. 코드 스니펫 규칙 (핵심이 보이게 — 필수)
- 실제 소스에서 가져오되 **핵심만** 잘라라. 곁가지는 `// ...`로 생략. 너무 길면 독자가 길을 잃는다.
- 파일 출처를 `<pre><span class="filename">crates/.../foo.rs</span><code>...</code></pre>`로 표시.
- **가장 중요한 줄(들)은 `<span class="hl">...</span>`로 감싸 하이라이트**하라. (왼쪽에 파란 띠가 생긴다.) 한 스니펫에 강조는 1~3줄로 절제.
- 덜 중요한 줄은 `<span class="dim">...</span>`로 흐리게 할 수 있다.
- 구문 색: `<span class="kw">`(키워드 fn/let/struct/pub), `<span class="ty">`(타입), `<span class="fn">`(함수명), `<span class="str">`(문자열), `<span class="num">`(숫자), `<span class="com">`(주석). 필수는 아니지만 가독성에 도움.
- **HTML 이스케이프 필수**: 코드 안의 `<` → `&lt;`, `>` → `&gt;`, `&` → `&amp;`. (Rust 제네릭 `Vec<u8>` 등에서 자주 실수한다. `&lt;u8&gt;`.)
- 한 챕터에 코드블록 2~4개면 충분. 코드 자체보다 **그 코드가 무슨 일을 하는지의 설명**이 본문이다.

## 7. 분량·상호참조
- 파트 2~6(fs·보안 핵심): 한 챕터 충실하게 (07 분량 = 좋은 기준, ±). 파트 7~8: 더 짧고 개관 위주.
- 앞/뒤 챕터를 `<span class="pill">N장 제목</span>`으로 가볍게 연결. 같은 걸 두 번 깊게 설명하지 말고 "자세히는 N장" 식으로 넘겨라.
- 다른 챕터가 아직 안 쓰였어도 상관없다. 번호로만 참조.

---

## 8. 챕터별 집필 명세
각 챕터: **핵심 개념(명사) · DB↔FS 다리 · 참고 소스/암묵지**. 개념은 "가르칠 대상", 소스는 "확인할 곳".

### 파트 1 · 출발점
- **01 감사 로그란, 왜 'DB 없이 파일로'인가** — 개념: 감사로그 vs 일반로그, tamper-evident, 임베디드 vs 외부DB, 부인방지/규제(HIPAA·SOX·GDPR). 다리: "보통 이런 건 DB/ELK에 넣는데 왜 프로세스 안 파일로?". 소스: 최상위 `README.md` 도입부, `SECURITY.md`.
- **02 지도와 DB↔파일시스템 대응표** — 개념: 5개 크레이트(core/middleware/server/client/mcp) 역할, 임베디드 모드 vs 서버 모드. **이 책 전체의 DB↔FS 대응표를 표로 제시**(WAL=로그, 데이터파일=세그먼트, 페이지체크섬=CRC, 락매니저=파일락, MVCC=읽기스냅샷, B-tree인덱스=인메모리인덱스, partition drop=세그먼트 unlink). 소스: `README.md` workspace layout, 각 crate `src/lib.rs` 모듈 문서.

### 파트 2 · 파일시스템 기본기 (깊게, 독자 약점)
- **03 파일·디렉토리·inode·디스크립터** — 개념: 파일=바이트열, 디렉토리=이름→inode 매핑, inode, file descriptor, 경로. 다리: "DB의 테이블/로우 대신 OS는 파일/바이트를 준다. 그 위에 구조를 우리가 얹는다." 소스: 일반 지식 + `store.rs` 디렉토리 레이아웃이 실제 디렉토리/파일로 어떻게 생기는지.
- **04 읽고 쓰기, rename의 원자성** — 개념: open/read/write/seek/append 모드, `rename(2)`의 원자적 교체, 디렉토리 fsync. 다리: "DB의 atomic commit을 우리는 atomic rename으로 흉내낸다." 소스: `storage/segment.rs`의 `OpenOptions`(create/truncate(false)/read/write), 어디서 rename을 쓰는지 grep.
- **05 page cache와 fsync** — 개념: write는 즉시 디스크가 아니다(page cache), `fsync`/`fdatasync`, 정전 시 유실 창, BufWriter(유저공간 버퍼)와의 2단 버퍼. 다리: "DB가 commit 때 fsync하는 그 동작을 우리가 직접 부른다." 소스: `storage/segment.rs` BufWriter·flush·sync, `store.rs` `SyncPolicy`. ※11장과 분담: 05는 fs 원리, 11은 정책.
- **06 std::fs 도구상자** — 개념: Rust `std::fs`/`std::io` API(File, OpenOptions, Read/Write/Seek, metadata, read_dir, remove_file, File::try_lock), OS 독립성. 다리: "이게 우리가 가진 연장 전부다. DB 엔진 없이 이걸로 다 만든다." 소스: 전 storage 모듈에서 실제 쓰인 std API 모으기, `Cargo.toml`의 MSRV 1.89(try_lock) 주석.

### 파트 3 · append-only 로그
- **07 (작성 완료 — 골드 스탠다드. 참고만)**
- **08 세그먼트 파일과 롤오버** — 개념: 로그를 여러 파일로 쪼갬, 세그먼트 번호, max_segment_bytes, 롤오버, sealed(불변) vs active(쓰는 중). 다리: "DB 데이터파일/테이블스페이스, LSM의 SSTable과 비슷. 왜 한 파일이 아니라 여러 개로?(삭제·백업·복제 단위)" 소스: `storage/mod.rs`, `storage/table.rs`(세그먼트 묶음=table), `store.rs` `max_segment_bytes`.
- **09 레코드 프레이밍·CRC32·magic/version** — 개념: 프레임 `[len][crc32][ts][payload]`, magic `ALOG`, FORMAT_VERSION, CRC=체크섬(우연 손상 탐지, 변조탐지 아님), MAX_RECORD 가드. 다리: "DB의 페이지 체크섬/torn page 탐지." 소스: `storage/segment.rs`(MAGIC, FORMAT_VERSION, FRAME_HEADER, MAX_RECORD, crc32fast, write_record/read).
- **10 직렬화: 구조체를 바이트로** — 개념: 직렬화/역직렬화, bincode(비자기서술적), serde, canonical bytes(해시·인덱스 키용 정규형), 왜 JSON을 문자열로 싸는지(ValueRepr). 다리: "DB는 타입별 바이너리 인코딩을 내부에 둠. 우리는 bincode로." 소스: `model.rs`(Value/ValueRepr/canonical_bytes, StoredValue), `Cargo.toml` bincode.

### 파트 4 · DB 보장을 파일로 재현 (본편, 깊게)
- **11 내구성: fsync 정책과 group commit** — 개념: 내구성 vs 처리량, `SyncPolicy::{Always,EveryN(n),OsManaged}`, group commit(N개 모아 한번 fsync), 성능 수치. 다리: "DB의 commit durability·group commit과 동일한 트레이드오프." 소스: `store.rs` SyncPolicy, README Performance 표.
- **12 원자성과 크래시 복구** — 개념: torn write(쓰다 만 마지막 레코드), 복구=세그먼트 스캔 후 망가진 꼬리 truncate, CRC로 부분쓰기 탐지, append-only라 redo만/undo 없음, base_index로 머클 위치 보존. 다리: "DB의 WAL replay·redo/undo. 여기선 redo-only가 왜 충분한가." 소스: `storage/segment.rs` `skim`(valid_len, 토른 테일), `storage/mod.rs` recovery 문단.
- **13 동시성 ①: single-writer + 파일 락** — 개념: single-writer 원칙, advisory file lock, `File::try_lock`(Rust 1.89), 루트 디렉토리 락으로 두 프로세스 동시 오픈 차단, 왜 단일 기록자가 변조탐지를 단순하게 만드나. 다리: "DB 락 매니저/한 줄 직렬화. 여기선 OS 파일 락 하나로." 소스: `store.rs`(try_lock, TryLockError), `Cargo.toml` MSRV 주석, client `src/lib.rs`(왜 단일 writer인지).
- **14 동시성 ②: 읽기 스냅샷과 MVCC** — 개념: copy-on-read 스냅샷(인메모리 인덱스 복제), 읽기는 쓰기를 막지 않음, 호출자 스레드에서 스캔. 다리: "DB의 MVCC/스냅샷 격리와 같은 목적(읽기-쓰기 비차단)을, 불변 세그먼트 + 인덱스 클론으로." 소스: `store.rs` `ReadSnapshot`, `pipeline.rs` snapshot, README "Snapshots".
- **15 인덱싱** — 개념: 보조 인덱스 없으면 풀스캔, 인메모리 레지스트리 인덱스(재시작 시 재구축), 디스크에 토큰 영속(FieldTokens), 엔티티 id/타입별 색인. 다리: "DB의 secondary index/B-tree. 여기선 인메모리 맵 + append된 토큰. 인덱스를 어떻게 영속·재구축하나." 소스: `registry.rs`(RegistryIndex, RegistryRecord.tokens, FieldTokens), `schema.rs` FieldIndex. ※블라인드 인덱스의 *암호학*은 26장, 여기선 *자료구조/영속* 관점.
- **16 쿼리 실행: 스캔과 커서 페이지네이션** — 개념: LogQuery, 세그먼트 순차 스캔 + 필터, 타깃 필터 AND, MatchMode, QueryPage 커서(keyset) 페이지네이션, 시간범위로 세그먼트 가지치기. 다리: "DB의 table scan vs index scan, LIMIT/OFFSET vs keyset pagination." 소스: `query.rs`, `store.rs` query 경로, `storage/table.rs`(TableScan, Position), 이슈 `쿼리 페이지네이션과 스캔 확장성`.
- **17 삭제와 보존: 세그먼트 unlink** — 개념: RetentionPolicy(days/max_bytes), 세그먼트 통째 삭제(unlink=O(1)), 행 단위 삭제/재작성 없음, 레지스트리는 보존(과거 렌더), active 세그먼트는 안 지움. 다리: "DB의 DELETE+vacuum(무겁다) vs partition drop(가볍다). 여기선 partition drop만." 소스: `retention.rs`, `store.rs` 리텐션, README Retention, 암묵지 운영 모니터링.
- **18 저장소 레이아웃과 포맷 버저닝** — 개념: root 디렉토리 구조(logs, registry/<type>, dlq, access, checkpoints), magic+version byte로 포맷 식별, 마이그레이션(v2 하드브레이크 사례). 다리: "DB의 카탈로그/시스템테이블·온디스크 포맷 버전." 소스: `store.rs` 레이아웃, `storage/segment.rs` FORMAT_VERSION, 암묵지 `디스크 포맷 진화`.

### 파트 5 · 무결성 (보안 ①, 깊게)
- **19 해시 함수와 SHA-256** — 개념: 암호학적 해시(일방향, 충돌저항, 눈사태효과), 디지털 지문, 같은 입력→같은 출력. 다리: "DB 체크섬은 우연 오류용(CRC), 암호학적 해시는 의도적 변조까지 탐지. 차이." 소스: `crypto.rs` sha256_hex, `merkle.rs` 해시 정의. ※9장 CRC와의 차이를 분명히.
- **20 머클 히스토리 트리 (RFC 6962)** — 개념: 해시 트리, 리프=레코드 해시, 내부노드=자식 해시의 해시, 루트 하나로 전체 커밋, RFC 6962 규칙(0x00 리프/0x01 내부), 증분 루트 유지. 다리: "전체 로그를 32바이트로 요약. 한 바이트만 바뀌어도 루트가 바뀐다." 소스: `merkle.rs`(MTH, leaf/interior hash, Roots), `merkle_log.rs`, 이슈 `Merkle 무결성 증명`.
- **21 포함 증명·일관성 증명** — 개념: inclusion proof(레코드가 트리에 있음, O(log n)), consistency proof(과거 트리가 현재 트리의 접두사=append-only 유지), 제3자 독립 검증(로그 전체 없이 루트+증명만). 소스: `merkle.rs`(inclusion_proof/verify_inclusion, consistency_proof/verify_consistency), `merkle_log.rs`(InclusionProof, ConsistencyProof), 암묵지 `무결성 검증 경계`.
- **22 체크포인트와 외부 앵커링** — 개념: 서명된 체크포인트(루트+서명), 외부 앵커링(신뢰 도메인에 루트 내보내기), truncation/전체 재작성 방어, AnchorHook. 다리: "DB 백업 검증을 넘어, 내부자(디스크 접근자)도 못 속이게." 소스: `checkpoint.rs`, `store.rs` AnchorHook, 이슈 `무결성 외부 앵커링`, README anchoring.
- **23 tamper-evident vs proof, 위협 모델** — 개념: 막는 것 vs 들키게 하는 것, 위협 모델, 신뢰 경계, blast radius, 무엇을 탐지하고 무엇을 못 막나(가용성·실시간차단은 범위 밖). 소스: `SECURITY.md`, README "What tamper-evidence covers", 암묵지 `무결성 검증 경계`.

### 파트 6 · 기밀성 (보안 ②, 깊게)
- **24 필드 보호 4단계** — 개념: 평문/SHA-256/HMAC/RSA, 필드별 선택(전역 스위치 없음), 검색성 트레이드오프(SHA·HMAC=정확일치, RSA=복호스캔), 저엔트로피 brute-force, 보호는 레지스트리 필드만(로그 컬럼은 평문). 다리: "DB의 TDE/컬럼 암호화. 근데 암호화하면 검색이 안 되잖아? → 다음 장." 소스: `schema.rs` FieldProtection, `model.rs` StoredValue, README "Field protection" 표.
- **25 대칭·비대칭·하이브리드 암호와 AEAD** — 개념: 대칭(AES-256-GCM)·AEAD(인증+기밀, 변조 시 복호 실패), 비대칭(RSA, 공개키 암호/개인키 복호), RSA-OAEP, 하이브리드 키 래핑(RSA로 AES키 감싸기), HMAC(키 있는 해시). 다리: "왜 RSA로 데이터를 직접 암호화 안 하나(느림·크기제한) → 하이브리드." 소스: `crypto.rs`(Aes256Gcm, Oaep, Hmac, KeyRing 전반).
- **26 블라인드 인덱스: 평문 없이 검색** — 개념: 검색 가능 암호화, 토큰화(소문자화·조각냄), Exact/Prefix(n)/Ngram(n) 인덱스, 토큰 다이제스트를 레코드 옆에 저장, 키로 토큰 생성(brute-force 표면 안 늘림) but 구조 누출. 다리: "암호화한 SSN을, 평문을 디스크에 안 남기고 부분검색. DB로는 어려운 일." 소스: `registry.rs`(tokens, FieldTokens), `schema.rs` FieldIndex, `tokens.rs`, 이슈 `검색 인덱스 옵션`, README "Blind indexes".
- **27 쓰기 전용 배포** — 개념: 개인키 없이 서버 기동, RSA 필드를 복호 불가 암호문으로 저장/반환, 클라이언트가 로컬 복호, blast radius 축소(서버 털려도 평문 못 봄). 다리: "DB 서버가 암호화 데이터를 들고 있지만 자기는 못 읽는 구조." 소스: server `src/lib.rs` key boundary, README "Write-only deployment", quipu-server README.
- **28 키 관리: 로테이션 vs 리키** — 개념: KeyRing 버전 키(최고버전=active, 옛버전=읽기용), 로테이션(싸다, 새 키 추가)과 re-key(비싸다, 유출 후 재암호화), HMAC은 재키 불가(일방향), 키 유실=복구불가/에스크로 없음, 서명키 격리. 소스: `crypto.rs` KeyVersion/KeyRing, `store.rs` RekeyEvent/RekeyedTable, README "Key management", 암묵지 `키 로테이션 운영`.

### 파트 7 · 쓰기·읽기 경로 (가볍게, 독자가 아는 영역)
- **29 비동기 파이프라인** — 개념: 논블로킹 emit, 바운디드 채널(sync_channel), 전용 writer 스레드, 백프레셔/QueueFull, cloneable handle, p50/p99 레이턴시. 다리: "프로듀서-컨슈머 큐. emit은 큐에 넣고 즉시 리턴." 소스: `pipeline.rs`(AuditPipeline, AuditHandle, sync_channel, QueueFull), middleware `lib.rs`. 짧게.
- **30 신뢰성: 재시도·백오프·DLQ·멱등성** — 개념: 재시도, 지수 백오프+지터, 멱등키, DLQ(디스크에 park, 재시작 생존, redrive, at-least-once), fallback 훅, 디스크풀 래치. 소스: `pipeline.rs`(DLQ/redrive), client `retry.rs`(Backoff, new_idempotency_key), README DLQ. 짧게.
- **31 tower 미들웨어** — 개념: tower Layer/Service(데코레이터), HTTP 요청을 감싸 자동 기록, EndpointRule(prefix/method/capture body), target_extractor(요청→타깃 추출). 다리: "Express/Spring 미들웨어와 같은 자리. 코드 거의 안 건드리고 감사." 소스: `layer.rs`(AuditLayer, EndpointRule), middleware README, `examples/axum-demo`. 짧게.
- **32 권한·필터·메타 감사** — 개념: RBAC(Role/Action Emit·Query·Administer), deny-by-default, pre/post 필터(요청 면제·이벤트 보강), 메타감사(접근로그=누가 읽었나, 별도 머클 spine, 자기참조 회피). 소스: `permissions.rs`, `filter.rs`, `access.rs`, 암묵지 `메타 감사`. 짧게.

### 파트 8 · 분산·운영 (개관)
- **33 단일 장애점과 가용성** — 개념: SPOF(단일 writer 데몬), 가용성 부담을 클라이언트로, 멱등 재전송, 디스크 스풀(다운 시 로컬 보관 후 재생), occurred_at 보존, 콜드 스탠바이 vs 라이브 페일오버. 소스: client crate(`lib.rs`, `spool.rs`, `retry.rs`), 암묵지 `가용성 모델`, quipu-server README cold-standby. 짧게.
- **34 수평 확장: 샤딩·읽기 복제** — 개념: 단일 writer 한계 → 샤딩(테넌트별 독립 트리), N배 쓰기, 전역순서 포기, ShardRouter(쓰기 라우팅·쿼리 fanout·타임스탬프 머지), 일관성 해싱, add-only 리샤딩, 읽기 복제(sealed 세그먼트 복사), 무상태 ingest. 소스: `middleware/sharding/*.rs`, `docs/specs/horizontal-scaling/solution-design.md`, 암묵지 `수평 확장 모델`. 개관 위주.
- **35 서버·클라이언트·MCP·관측성** — 개념: 서버 모드(토큰 인증 HTTP/JSON, RBAC, write-only), 클라이언트 요약, MCP(LLM 감사관, JSON-RPC, query/history/verify 툴, 자기 조회도 감사됨), 관측성(Prometheus /metrics, healthz, lock-free 레이턴시 히스토그램, syslog/SIEM, NDJSON export). 소스: server/client/mcp 각 crate, `metrics.rs`/`health.rs`, 암묵지 `MCP 감사관`·`운영 모니터링`. 개관 위주, 각 주제 짧게.
