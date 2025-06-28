# 🤖 aidabang

**AI 도구 모음 서비스** - 특정 용도에 딱 맞는 AI 웹 서비스들의 모음

## 📋 프로젝트 개요

aidabang은 GPT, DALL·E, 미드저니 등의 AI API를 활용하여 특정 용도에 최적화된 소형 웹 서비스들을 제공하는 플랫폼입니다.

### 🎯 핵심 특징

- **목적 특화 소형 웹앱**: 특정 용도에 딱 맞는 AI 도구들
- **직관적인 UI/UX**: 프롬프트 설계 없이 누구나 쉽게 사용
- **빠른 출시 / 반복 개선**: MVP → 사용자 반응 → 빠른 피드백 적용

## 🛠 제공 도구

| 도구 | 상태 | 설명 |
|------|------|------|
| 💌 **AI 연애편지 작성기** | ✅ 완료 | 로맨틱한 연애편지 자동 생성 |
| 📄 **한류 스타일 이력서 생성기** | 🚧 개발중 | 한국식 감성의 이력서 작성 |
| 🎨 **미드저니 프롬프트 도우미** | 🚧 개발중 | 최적화된 미드저니 프롬프트 제안 |
| 📱 **틱톡 자막 생성기** | 🚧 개발중 | 유행 문체 자막 및 스크립트 생성 |
| 🎭 **드라마 대사 생성기** | 🚧 개발중 | 드라마 스타일 대사 생성 |

## 🚀 시작하기

### 1. 저장소 클론

```bash
git clone https://github.com/your-username/aidabang.git
cd aidabang
```

### 2. 가상환경 생성 및 활성화

```bash
# Python 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정

`.env` 파일을 생성하고 필요한 API 키를 설정하세요:

```env
# OpenAI API 설정
OPENAI_API_KEY=your_openai_api_key_here

# Anthropic API 설정 (Claude)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# 앱 설정
APP_ENV=development
DEBUG=True
LOG_LEVEL=INFO
```

### 5. 애플리케이션 실행

```bash
streamlit run app.py
```

브라우저에서 `http://localhost:8501`로 접속하여 서비스를 이용하세요.

## 📁 프로젝트 구조

```
aidabang/
├── app.py                      # Streamlit 메인 애플리케이션
├── requirements.txt            # Python 의존성
├── .gitignore                 # Git 무시 파일
├── README.md                  # 프로젝트 문서
├── src/                       # 소스 코드
│   ├── __init__.py
│   ├── config/                # 설정 관리
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── tools/                 # AI 도구들
│   │   ├── __init__.py
│   │   └── love_letter_generator.py
│   └── utils/                 # 유틸리티
│       ├── __init__.py
│       └── ai_client.py
├── tests/                     # 테스트 코드
└── docs/                      # 문서
```

## 🎨 사용 예시

### AI 연애편지 작성기

1. 사이드바에서 "AI 연애편지 작성기" 선택
2. 받는 사람, 보내는 사람, 연애 기간 입력
3. 편지 톤과 종류 선택
4. 특별한 날이나 추가 메시지 입력 (선택사항)
5. "편지 작성하기" 버튼 클릭
6. AI가 생성한 로맨틱한 편지 확인

## 🔧 기술 스택

- **Backend**: Python 3.8+
- **Web Framework**: Streamlit
- **AI APIs**: OpenAI GPT, DALL-E, Anthropic Claude
- **Package Management**: pip
- **Version Control**: Git

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 📞 연락처

프로젝트 링크: [https://github.com/your-username/aidabang](https://github.com/your-username/aidabang)

## 🙏 감사의 말

- OpenAI와 Anthropic의 AI API 제공
- Streamlit 팀의 훌륭한 웹 프레임워크
- 모든 기여자분들

---

**aidabang** - AI로 만드는 특별한 도구들 🤖✨