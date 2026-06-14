# Quipu-Log 교과서

📖 **읽기: https://draft-dhgo.github.io/quipu-log-textbook/ko/**

[English](README.md) | 한국어

[Quipu-Log](https://github.com/draft-dhgo/Quipu-Log)(변조-탐지 감사 로그)를 기능이 아니라 **개념**으로 이해하기 위한 HTML 교과서. 저장 엔진과 보안 모델을, 이미 아는 DB 지식을 사다리 삼아 모르는 파일시스템 구현으로 건너가며 배운다.

- **8파트 35챕터** — 출발점 / 파일시스템 기본기 / append-only 로그 / DB 보장을 파일로 / 무결성 / 기밀성 / 쓰기·읽기 경로 / 분산·운영
- 외부 의존 0, 자체 완결형. `index.html`을 브라우저로 열면 된다.
- 이중 언어: 영문은 루트, 한글은 [`/ko/`](https://draft-dhgo.github.io/quipu-log-textbook/ko/).

## 빌드

본문 조각은 `bodies/<lang>/NN-slug.html`, 공용 셸·목차는 `build.py`가 생성한다.

```sh
python3 build.py   # manifest.json + bodies/{en,ko}/ → 영문 /, 한글 /ko/
```
