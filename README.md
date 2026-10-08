# 바이오프로테크 홈페이지 — 261008 수정시안 (TF 1차 회의 반영)

## 샘플시안 → 261008 수정시안 변경 사항

- 상단 메뉴: 회사소개 · 뉴스 · 제품(중앙) · 자료실 · 고객지원 · 문의 (`assets/js/chrome.js`)
- 하단 SNS 5종: Instagram · WeChat · TikTok · LinkedIn · YouTube (새 탭). 공식 계정 확정 시 `chrome.js`의 `SNS_LINKS` url만 교체
- 회사소개 서브탭: 회사소개(`about.html`) / 품질방침(`quality.html`) / 인증현황(`certification.html`, 신규)
- 품질방침: 선언문·세부항목은 품질팀 확정본 대기(자리표시), QMS(ISO 13485 · KGMP · FDA QMSR) 표기
- 인증현황: 국가별 인증 현황 표(인증팀 261001) + 인증서 49건 열람(옌타이 BPC 중국 등록증 2건 포함)(필터·확대 뷰어·이전/다음·키보드·스와이프)
- 이미지: `assets/img/certs/full`·`thumb` (출처: 홈페이지_인증서_게시용_수정)
- FDA 510(k) 3건 「게시 보류 검토」 배지 — 숨기려면 `certification.html`의 `SHOW_ON_HOLD = false`
- 수출용 허가 7건 「수출용」 배지
- 메인 인증 섹션: 배지 클릭 시 해당 인증서로 이동 + 「인증서 전체 보기」 버튼
- 뉴스 서브탭: 뉴스 · IR / 전시회 · 학회(`news/exhibition.html`, 신규) — 연도별 일정 카드, 상태(참가 예정·일정 확인 중·종료), 뉴스의 「전시회」 태그 글 연동. 일정은 페이지 내 `EXHIBITIONS` 배열 수정 (현재 [예시] 3건)
- 자료실: 인증서·SDS 탭 삭제, 제품 카탈로그 PDF 4종 게시(`assets/catalog/`, 전기수술 카탈로그는 웹용 압축 19MB→3.3MB)
- 전시회: 2026 GMES(실제 개최 정보, 9/3–4 원주) + 2026 MEDICA(가상 데이터, 「가상」 배지) 일정·뉴스 추가
- 인증현황: 인증서 이미지 → 국가별 현황 표 순서로 변경
- 제품: 카탈로그 4종 기반 사양을 `products.json`에 반영(설명·특징·주요 사양·포장 단위·모델 표·이미지), 상세 페이지 모델 검색, 카탈로그 바로보기
- 제품 이미지: `assets/img/products/` (카탈로그에서 추출)
- 카테고리 페이지 버그 수정(제목 설정 시 스크립트 중단 → 제품 목록이 비던 문제)
- 카탈로그 없는 제품(SpO₂ Sensor, TENS Electrode/Unit, EMS Unit, IF Unit)은 「카탈로그 준비 중」 표시
- 메인 글로벌 섹션(261008): 어두운 배경 → 밝은 톤, 세계지도를 실제 국가 경계 SVG로 교체(Natural Earth 110m, 태평양 중심). 수출 60개국 하이라이트 + 본사→각국 연결선, 통계(60개국·5개 권역·해외 거래처 160+·4개 법인), 권역별 국가 목록(지도와 마우스 연동). 출처: `2026 MEDICA/거래국가_목록.xlsx` (2022.10~2026.10 수주 기준)
- 글로벌 섹션 2차: 진한 파랑 팔레트(수출국 #1d5fd1, 본사·법인 마커 레드), 국가 마커 확대, 국가 목록을 「권역 탭(전체 60·유럽 23·아태 16·중동 9·미주 8·아프리카 4) + 다단 목록」으로 변경 — 탭 선택 시 지도에서 해당 권역만 강조
- 헤더 로고: 영상 위 투명 헤더 상태에서 흰색으로 표시(스크롤 시 원래 색) — `theme-apple.css`
- 메인 텍스트: 문단 폭 확대로 한 줄 우선 표시, 긴 문장은 문장·구 단위 줄바꿈(`<br class="pc">`, 모바일에서는 해제) + 한글 단어 단위 줄바꿈(keep-all)
- 표기 원칙: 글자 사이 장식용 대시(—, –, " - ") 사용 금지. 기존 문구는 쉼표·콜론·괄호·가운뎃점(·)으로 바꾸고, 날짜 범위는 물결표(~) 사용. 모델번호 안의 하이픈(예: BE1227P-05)은 유지
- 자료실: 제목 Resources & Downloads → Download, 「마케팅 자료」 탭 → 「사용설명서(IFU)」 탭(파일 준비 전 빈 상태 안내). 영문 메뉴명도 Download
- 뉴스: 제목 News & Press → News
- 사이트 검색: 전 페이지 헤더에 검색 버튼(단축키 /). 제품명·모델번호(예: BE1227P, T716)·사양·뉴스·FAQ·주요 페이지 통합 검색, 한글 일반어 동의어 확장(심전도→ECG, 접지판→Grounding Pad 등). 동의어는 `chrome.js`의 `SR_SYN`에서 추가. 전체 결과는 `search.html?q=`
- 품질방침: 품질팀 「품질방침& 목표.bmp」 내용 반영(방침 선언문, 품질목표 4항목, 최종 목표). 대표이사 이름은 게시하지 않음. 디자인 요소: 방침 배지 아이콘, 품질목표 벤다이어그램(3개 목표 교집합 = 품질목표 달성, 바깥 순환 화살표 = 지속적 개선), 목표별 픽토그램 카드, PDCA 개선 사이클
- 색상: 밝은 파랑(#0071e3 등) 전부 남색 계열로 교체. 기본 강조색 #14306b, 진한 남색 #0f2655, 지도 수출국 #1e3a75 (`colors_and_type.css`의 --bp-accent1/5 포함)
- 디자인 원칙(261008): 흔한 AI풍 장식 사용 금지. 둥근 카드 위쪽/왼쪽 강조색 띠, 마우스 올릴 때 카드가 떠오르는 효과(그림자+이동), 장식용 그라데이션·원형 무늬, 아이콘을 둥근 색 타일에 넣는 방식, 제목 위 아이콘 배지, 큰 그림자 패널, 점 주변 발광 효과는 쓰지 않음. 대신 가는 구분선(헤어라인), 단색 면, 테두리 색 변화로 표현
- 페이지 상단 설명문(lead): 가는 글씨(300), 줄간격 1.55, 문장마다 줄바꿈, 최대 2문장, 문장당 1줄(한글 약 40자·영문 약 85자 이내). 제품 카테고리 설명도 동일 기준으로 축약
- 하위 페이지 상단(page-hero): 높이 축소(상 180→128px, 하 80→44px, 최소높이 해제), 배경 검정 그라데이션 → 검정에 가까운 남색 단색 #0a1428 (제품 메가메뉴·메인 카테고리 패널·하단 footer·플로팅 버튼도 동일 색). 하단(footer) 배경 #eef1f6(남색과 어울리는 차가운 회색)
- 뉴스: 기존 사이트(protechsite.com) NEWS & IR 게시글 13건 전체 이전(2022.10~2026.09, 「IR 공시」 태그, 원문 그대로). 기존 예시 게시글 삭제, 목록 10건 단위 페이지 나눔, 상세에 본문 전체·표 표시. YouTube 링크를 공식 채널(@bioprotech_official)로 연결
- 회사소개(about.html): 01 Company Introduction(큰 헤드라인+소개 4문장, 21:9 회사 영상, 핵심 수치 2000·60·4·OEM/ODM/OBL) / 02 Product Portfolio(제품 사진 4종, assets/img/about) / 03 How We Work(남색 전폭 밴드: OEM·ODM·OBL·Direct Supply) / 04 Our Commitments(큰 번호 01~03) / 05 CEO Message(연회색 밴드, 인용부호 타이포). 대표이사 이름 미기재
- 전시회·학회: classys.co.kr 전시/학회 레이아웃 참고로 재구성(연도 탭, 포스터형 카드 3열, 위치·날짜·부스, 더보기, 9개 단위 페이지). 포스터 이미지는 EXHIBITIONS의 img에 경로 지정(없으면 남색 타일에 행사명)
- 데이터 묶음: `assets/js/data-bundle.js`(뉴스·제품·FAQ·번역 JSON 포함)를 전 페이지에서 먼저 불러와, 파일을 더블클릭(file://)으로 열어도 뉴스·제품이 표시됨. JSON 수정 후 `python build-data.py` 한 번 실행 필요
- 전시회 MEDICA 2026 카드 이미지: 부스 예상시안 01 ver.2 렌더(assets/img/exhibitions/medica-2026.jpg), 부스 Hall 10 / 10D30(시안 표기 기준)
- 전체 제품 페이지(products/index.html): 4개 대분류 카드를 한 줄에(태블릿 2열). 대표 제품 1개 이미지(1200×900, 흰 배경): ESU=Evacuator_Front.png, ECG=T716.jpg(앞면), Neuro=신경진단 카탈로그 EMG 니들 사진(배경 평탄화), Pain=MAXTENS2000.jpg(1대). 원본: 홈페이지/자료
- GMES 2026 뉴스: 이미지 중심 기사로 변경(대표 이미지 KO/EN, 2층 부스 안내도, 핵심 정보 표, 현장 사진 3장). 이미지 원본: D:\Claude\전시회\2026_GMES (GMES_Shorts_260818-03·04·06·07·08, 홈페이지_부스팝업_시안). 부스 W209(2F)로 정정. 뉴스 항목에 lead/facts/gallery 필드 추가(다른 뉴스에도 같은 방식으로 사용 가능)
- 제품 이미지 전면 교체(261008): 자료 폴더 원본 제품 사진(글자·지시선 없음) 기준, 1200×900 흰 배경 통일, 21개 제품 54장. 원본이 없는 신경진단 5종·Smoke Adapter는 카탈로그 PDF 안의 원본 사진을 추출(배경 정리)해 사용. SpO₂·TENS 전극/Unit·EMS·IF Unit 이미지 신규 추가
- 카탈로그 옮기며 확인 필요 사항: `../카탈로그_사양정리_확인사항_261008.md`

---

# 바이오프로테크 홈페이지 v3-3-6 — Apple 스타일

v3-1 Apple Design System 토큰(흰 캔버스 + 잉크 블랙 #1d1d1f + Apple Blue #0071e3 단일 액센트 + 시네마틱 다크 히어로 + 980px 필 버튼 + 18px 라운드 카드 + 라이트 푸터)을 유지하되, 메인 페이지를 단(段) 구조로 재구성한 버전. 테마는 `Bioprotech Design System/colors_and_type.css`(토큰)와 `assets/css/theme-apple.css`(컴포넌트 오버라이드) 두 파일로 구성됨.

## v3-3-5 → v3-3-6 변경 사항

- **스페인어(ES) 추가** — 기존 한국어(KO)/영문(EN) 2개 언어에 **스페인어**를 더해 3개 언어 지원. 헤더 언어 토글에 `ES` 버튼 추가(KO / EN / ES), `localStorage`로 선택 유지.
- **적용 범위** — 전체 페이지. 공통(헤더·내비게이션·푸터, `chrome.js`)과 메인 페이지, 하위 페이지(회사소개·연혁·글로벌·연구개발·품질·제품·뉴스·자료실·고객지원·문의·검색·약관·404) 본문, 데이터 파일(`products.json`·`news.json`·`faq.json`)·`i18n.json`까지 스페인어 번역 포함.
- **메커니즘** — 본문은 `.es-only` 클래스(`site.css`의 `body[data-lang="es"]` 표시 규칙), 데이터는 각 다국어 객체에 `es` 키, JS UI 문자열은 3개국어 분기로 처리.
- ※ 스페인어 번역은 기계 번역 초안 수준이므로, 공개 전 원어민/전문 검수 권장.

## v3-3 → v3-3-5 변경 사항

- **폰트 통일** — 본문·제목을 모두 **Pretendard**로 적용. 제목용 IBM Plex Sans KR 참조(`--bp-font-head`)와 웹폰트 `@import`를 제거하고, 모노(IBM Plex Mono)만 유지.

## v3-2 → v3-3 변경 사항

- **히어로 텍스트 중앙정렬** — 최상단 이미지 위 태그·제목·설명·버튼·인디케이터를 중앙 정렬.
- **히어로 설명 문구 축소** — 가운데 설명을 한 줄(KO/EN 각 1문장)로 정리.
- **헤더 로고 교체** — 좌측 상단 "BP" 텍스트 마크를 바이오프로테크 실제 로고 이미지(`assets/img/bioprotech-logo.png`, 흰 배경을 투명 처리)로 변경.
- **헤더 워드마크 정리** — 로고 옆 표기를 영문 "Bioprotech"만 남기고 하단 "Bio sensors & Bio products" 보조 문구 삭제.
- 글로벌 섹션 세계지도(반전 이미지 + 진출국 마커)·폰트·단 구조 등 v3-2 구성은 그대로 유지.

## v3-1 → v3-2 변경 사항

- **좌측 고정 사이드박스 제거** — 메인 페이지의 2단(사이드바 + 콘텐츠) 그리드를 전폭(full-width) 레이아웃으로 전환. 사이드바 전용 폰트·텍스트도 함께 제거.
- **전체 폰트 교체** — Bioprotech Research PPTX 디자인 폰트 적용: 본문 Pretendard, 제목 IBM Plex Sans KR, 모노 IBM Plex Mono. `colors_and_type.css`의 `--bp-font-family`·`--bp-font-head`로 전 페이지에 일괄 적용됨.
- **메인 페이지 단 구조** — ① 히어로(배경 이미지 순차 전환 + 제품 카테고리 탭) → ② 회사 설명 + 통계 → ③ 글로벌 진출 현황(세계지도 + 4개 법인) → ④ 뉴스·공지(`news.json` 연동) → ⑤ 인증 현황 → 하단 푸터(회사 주소).
- **세계지도** — 진출국(한국·미국·중국 연태/광저우)을 마커로 표시한 인라인 SVG. 배경 그라데이션·위경도 그리드·거점 연결선·펄스 애니메이션 포함.
- 배경 이미지 순차 전환(5초)·언어 스위처(KO/EN)·반응형 등 기존 기능은 그대로 유지.

---

## 실행 방법

CORS 제한으로 JSON fetch가 `file://`에서 차단되므로 로컬 HTTP 서버로 실행 필요.

```bash
# Python 3
python -m http.server 8000

# Node.js
npx serve .
```

브라우저에서 `http://localhost:8000/` 접속.

---

## 파일 구조

```
/
├── index.html                  메인 홈
├── search.html                 통합 검색
├── 404.html                    에러 페이지
├── sitemap.xml · robots.txt    SEO
│
├── products/
│   ├── index.html              전체 제품 카탈로그
│   ├── category.html?cat=xxx   카테고리별 목록
│   └── detail.html?id=xxx      제품 상세 (21건 데이터 연동)
│
├── company/
│   ├── about.html              회사소개
│   ├── history.html            연혁
│   ├── global.html             글로벌 네트워크
│   ├── rnd.html                연구개발
│   └── quality.html            품질·인증
│
├── news/
│   ├── index.html              뉴스 목록 (태그 필터)
│   └── detail.html?id=xxx      뉴스 상세
│
├── support/
│   ├── faq.html                FAQ (카테고리·검색)
│   └── contact.html            문의 양식
│
├── downloads/
│   └── index.html              자료실
│
├── legal/
│   ├── privacy.html            개인정보처리방침
│   └── terms.html              이용약관
│
├── assets/
│   ├── css/site.css            공통 스타일 (헤더·푸터·폼 등)
│   ├── js/chrome.js            공통 크롬 주입 (i18n·mobile nav·lang toggle)
│   └── data/
│       ├── products.json       21개 제품 데이터
│       ├── news.json           뉴스 스텁
│       ├── faq.json            8개 FAQ
│       └── i18n.json           KO/EN 사전
│
└── Bioprotech Design System/   원본 디자인 시스템 (건드리지 않음)
    ├── colors_and_type.css     컬러 토큰 + 타입 스케일
    └── assets/                 로고·히어로·제품 placeholder 이미지
```

---

## 구현된 기능

- 공통 헤더·푸터 자동 주입 (`chrome.js`)
- **언어 스위처 KO ↔ EN** — localStorage 저장, 전체 페이지 텍스트 전환
- 모바일 햄버거 메뉴
- 메인 히어로 슬라이드쇼 (5초 자동 전환)
- 제품 데이터 구동 — 카탈로그 → 카테고리 → 상세 3단계 네비게이션
- 뉴스 태그 필터
- FAQ 카테고리 탭 + 실시간 검색
- 통합 검색 (제품·뉴스·FAQ 교차 검색 + 하이라이트)
- 문의 폼 — 유효성 검증, 제품 드롭다운 자동 생성, 성공/에러 피드백
- 반응형 (900px 이하 모바일 레이아웃)
- SEO — sitemap.xml, robots.txt, 페이지별 meta description
- 404 페이지

---

## 공란(콘텐츠 대기 중) 항목

콘텐츠가 확정되지 않은 영역은 `.placeholder-empty` 또는 `.placeholder-img` 컴포넌트로 표시됨.

### 공란 처리된 항목
- **제품 상세**: 메인 이미지 4종, 스펙 테이블 7개 필드, 설명 본문, 카탈로그/SDS PDF
- **회사소개**: CEO 초상 사진, 대표이사 메시지 본문, 대표이사 성명
- **글로벌**: 미국·중국 3개 법인 주소, 지도 embed
- **품질·인증**: 인증서 PDF 다운로드 링크
- **자료실**: 카탈로그·SDS·인증서·마케팅 자료 PDF 전체
- **뉴스**: 본문 콘텐츠 (제목·요약만 스텁으로 존재)
- **개인정보처리방침**: 개인정보 보호책임자 정보
- **로고**: BP 텍스트 워드마크 플레이스홀더 (실 로고 PNG 대체 필요)

### 반영 방법
- `assets/data/products.json` — 제품별 `description`, `specs`, `images`, `downloads` 필드 추가
- `assets/data/news.json` — `body` 필드(HTML) 추가
- `products/detail.html` — 이미지 placeholder를 실제 `<img src>`로 교체
- `company/about.html` — CEO 메시지 영역의 placeholder를 텍스트로 교체

---

## 문의 폼 실제 전송

현재 `support/contact.html`의 폼 제출은 콘솔 출력 + 성공 메시지만 표시하는 데모 상태.
실 서비스에 연결하려면 다음 중 하나 선택:

1. **Formspree** — `<form>` 태그의 action을 `https://formspree.io/f/{FORM_ID}`로 교체
2. **Resend / SendGrid API** — 서버리스 함수(Vercel/Cloudflare Workers)에 폼 데이터 전달
3. **자체 SMTP** — 서버 측 `/api/inquiry` 엔드포인트 구현

`support/contact.html` 하단 스크립트의 `fetch(...)` 주석 처리된 라인을 해제하고 URL 지정.

---

## 다음 단계 권장

1. 제품 사진 21종 수급 및 업로드
2. 카탈로그·SDS PDF 수급 및 `assets/downloads/` 게시
3. 문의 폼 백엔드 연동 (Formspree 권장)
4. Google Analytics 4 스니펫 삽입
5. 실 도메인 + Vercel/Cloudflare Pages 배포
6. 법무 검토 후 privacy/terms 본문 확정
