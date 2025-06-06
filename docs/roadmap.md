# TradeMatch.AI 개발 로드맵 & 진행 기록

## ✅ 전체 프로젝트 로드맵 (할 일 정리)

### 1단계: 기획 & 구조 설계 (D-40 ~ D-36)
- 프로젝트 목적, 사용자 시나리오 문서 작성
- [서비스 흐름도 작성](./service_flow.md) [ ✅ ] - 250606
- Hugging Face에서 사용할 모델 후보 정리 (flan-t5-base, mistral-7B 등)
- API 정보 수집 및 테스트 (data.go.kr)

### 2단계: 데이터 수집 및 전처리 (D-35 ~ D-30)
- 산업통상자원부 API 신청 및 인증키 발급
- Python 코드로 API 호출 테스트 (fetch_trade_data.py)
- 받은 데이터를 JSON 형식으로 저장 (sample_input.json)
- 수출 품목 → HS 코드 자동 변환 함수 만들기 (선택 사항)

### 3단계: LLM 연동 기능 개발 (D-29 ~ D-20)
- Hugging Face 모델 로딩 테스트 (model_loader.py)
- 바이어 추천 요약 생성 로직 구현 (recommend.py)
- 커뮤니케이션 이메일 생성 (email_generator.py)
- 프롬프트 템플릿 관리 (prompt_templates.py)
- 테스트용 입력/출력 노트북 작성 (test_prompt.ipynb)

### 4단계: 백엔드 API 구축 (D-19 ~ D-14)
- FastAPI or Flask 서버 구조 세팅 (main.py)
- 사용자 입력 받는 API 작성 (/recommend, /email)
- CORS 설정, 에러 핸들링 등 기본 구성
- LLM 결과 반환 API와 연결

### 5단계: 프론트엔드 구축 (D-13 ~ D-8)
- 사용자 입력 폼 (회사 정보, 수출 품목 등)
- 추천 바이어 결과 카드 UI
- 이메일 보기 + 복사 기능
- axios 등으로 백엔드 API 연동

### 6단계: 통합 테스트 & 디버깅 (D-7 ~ D-4)
- 전체 시나리오 테스트 (입력 → 결과까지)
- LLM 출력이 적절한지 확인 및 개선
- 예외 상황 (데이터 없음, 이상값 등) 처리

### 7단계: 문서화 & 발표 준비 (D-3 ~ D-Day)
- README.md 문서 작성 (소개, 기능, 실행 방법 등)
- 시연용 Demo 영상 or 이미지 준비
- 발표용 슬라이드 (요약 + 핵심 기능 + 기술 설명)
- 향후 개선 방향 작성

---

## 📅 진행 상황/메모/회고
- 각 단계별 진행 상황, 이슈, 회고, 개선점 등을 자유롭게 추가 기록
- 예시)
  - 2025-06-06: docs/roadmap.md 파일 생성 및 로드맵 정리
  - ...
