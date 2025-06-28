"""
aidabang - AI 도구 모음 서비스
Streamlit 웹 애플리케이션
"""
import streamlit as st
import sys
import os
import math

# 프로젝트 루트를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.config.settings import settings
from src.tools.love_letter_generator import love_letter_generator

def main():
    """메인 애플리케이션"""
    # 밝은 테마 적용 (Streamlit 1.10+)
    st.set_page_config(
        page_title="aidabang - AI 도구 모음",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={}
    )
    # 밝은 배경 스타일 및 폰트 적용
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&family=Nanum+Gothic:wght@400;700&display=swap');
        body, .stApp {
            background: #f7f8fa !important;
            font-family: 'Noto Sans KR', 'Nanum Gothic', sans-serif !important;
        }
        .block-container {
            padding-top: 2rem;
        }
        .aidabang-title {
            color: #222 !important;
            font-size: 2.2rem !important;
            font-weight: 800 !important;
            letter-spacing: -2px;
            margin-bottom: 0.2em;
            display: flex;
            align-items: center;
        }
        .aidabang-title-emoji {
            font-size: 2.2rem;
            margin-right: 0.3em;
        }
        .aidabang-status {
            color: #222 !important;
            font-weight: 700;
        }
        /* 반응형 카드 */
        @media (max-width: 1200px) {
            .stApp [data-testid="column"] > div > div {
                min-width: 220px !important;
                font-size: 0.97em !important;
            }
        }
        @media (max-width: 900px) {
            .stApp [data-testid="column"] > div > div {
                min-width: 180px !important;
                font-size: 0.92em !important;
            }
        }
        @media (max-width: 700px) {
            .stApp [data-testid="column"] > div > div {
                min-width: 120px !important;
                font-size: 0.85em !important;
            }
            .aidabang-title { font-size: 1.3rem !important; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # 사이드바 (간소화)
    with st.sidebar:
        st.title("🤖 aidabang")
        st.markdown("AI 도구 모음 서비스")
        st.divider()
        if settings.validate_api_keys():
            st.success("✅ API 키 설정 완료")
        else:
            st.error("❌ API 키 설정 필요")
            st.info("환경 변수에 API 키를 설정해주세요.")
        if st.button("🏠 홈으로 돌아가기"):
            st.session_state.current_tool = None
            st.rerun()
    if 'current_tool' not in st.session_state:
        st.session_state.current_tool = None
    if st.session_state.current_tool:
        show_selected_tool(st.session_state.current_tool)
    else:
        show_home_page()

def show_home_page():
    st.markdown('<div class="aidabang-title"><span class="aidabang-title-emoji">🤖</span>aidabang</div>', unsafe_allow_html=True)
    st.markdown("### AI로 만드는 특별한 도구들")
    st.markdown("목적 특화 AI 웹 서비스 모음")
    gradients = [
        "linear-gradient(135deg, #f8ffae 0%, #43c6ac 100%)",
        "linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%)",
        "linear-gradient(135deg, #fad0c4 0%, #ffd1ff 100%)",
        "linear-gradient(135deg, #c2ffd8 0%, #465efb 100%)",
        "linear-gradient(135deg, #fcb69f 0%, #ffecd2 100%)",
    ]
    tools = [
        {"name": "AI 연애편지 작성기", "emoji": "💌", "description": "AI가 당신의 마음을 담아 로맨틱한 연애편지를 작성해드립니다.", "status": "✅ 완료", "features": ["5가지 편지 톤", "5가지 편지 종류", "개인화된 내용"]},
        {"name": "한류 스타일 이력서 생성기", "emoji": "📄", "description": "한국식 감성과 스타일로 이력서를 자동 작성합니다.", "status": "🚧 개발중", "features": ["한국식 감성", "업종별 맞춤", "ATS 최적화"]},
        {"name": "미드저니 프롬프트 도우미", "emoji": "🎨", "description": "그림 주제 입력 시 최적화된 미드저니 프롬프트를 제안합니다.", "status": "🚧 개발중", "features": ["스타일 최적화", "상세 프롬프트", "예시 이미지"]},
        {"name": "틱톡 자막 생성기", "emoji": "📱", "description": "유행 문체로 짧은 영상용 자막과 스크립트를 생성합니다.", "status": "🚧 개발중", "features": ["트렌디 문체", "해시태그 제안", "길이 조절"]},
        {"name": "드라마 대사 생성기", "emoji": "🎭", "description": "특정 상황에서의 드라마 스타일 대사를 생성합니다.", "status": "🚧 개발중", "features": ["장르별 스타일", "감정 표현", "상황별 맞춤"]}
    ]
    cols = st.columns(5)
    for idx, tool in enumerate(tools):
        col = cols[idx % 5]
        grad = gradients[idx % len(gradients)]
        with col:
            st.markdown(f"""
            <div style="
                background: {grad};
                padding: 28px 18px 18px 18px;
                border-radius: 18px;
                margin: 12px 0 24px 0;
                box-shadow: 0 2px 10px rgba(0,0,0,0.07);
                color: #222;
                min-height: 240px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                font-family: 'Noto Sans KR', 'Nanum Gothic', sans-serif;
            ">
                <h3 style="margin: 0 0 14px 0; font-size: 1.35em; font-weight: 700; letter-spacing: -1px; color: #222; text-align: center;">
                    {tool['emoji']} {tool['name']}
                </h3>
                <p style="margin: 0 0 14px 0; font-size: 1.08em; opacity: 0.95; font-weight: 500; color: #222; text-align: center;">
                    {tool['description']}
                </p>
                <div style="margin: 0 0 12px 0; text-align: center;">
                    <span class='aidabang-status' style="background: rgba(255,255,255,0.35); padding: 4px 14px; border-radius: 10px; font-size: 1em; font-weight: 700; color: #222;">
                        {tool['status']}
                    </span>
                </div>
                <ul style="margin: 0 0 10px 0; padding-left: 0; font-size: 1em; opacity: 0.90; list-style: none; color: #222; text-align: center;">
            """, unsafe_allow_html=True)
            for feature in tool['features']:
                st.markdown(f"<li style='margin-bottom:2px;'>{feature}</li>", unsafe_allow_html=True)
            st.markdown("</ul>", unsafe_allow_html=True)
            if tool['status'] == "✅ 완료":
                if st.button(f"🚀 {tool['name']} 사용하기", key=f"btn_{idx}"):
                    st.session_state.current_tool = tool['name']
                    st.rerun()
            else:
                st.button(f"🔒 {tool['name']} 준비중", key=f"btn_{idx}", disabled=True)
            st.markdown("</div>", unsafe_allow_html=True)

def show_selected_tool(tool_name):
    if tool_name == "AI 연애편지 작성기":
        show_love_letter_generator()
    elif tool_name == "한류 스타일 이력서 생성기":
        show_resume_generator()
    elif tool_name == "미드저니 프롬프트 도우미":
        show_midjourney_helper()
    elif tool_name == "틱톡 자막 생성기":
        show_tiktok_generator()
    elif tool_name == "드라마 대사 생성기":
        show_drama_generator()

def show_love_letter_generator():
    st.title("💌 AI 연애편지 작성기")
    st.markdown("AI가 당신의 마음을 담아 로맨틱한 연애편지를 작성해드립니다.")
    with st.form("love_letter_form"):
        col1, col2 = st.columns(2)
        with col1:
            recipient_name = st.text_input("받는 사람 이름", placeholder="예: 민수")
            sender_name = st.text_input("보내는 사람 이름", placeholder="예: 영희")
            relationship_duration = st.text_input("연애 기간", placeholder="예: 1년 3개월")
        with col2:
            tone_options = love_letter_generator.get_tone_options()
            tone = st.selectbox("편지 톤", list(tone_options.keys()), format_func=lambda x: tone_options[x])
            letter_type_options = love_letter_generator.get_letter_type_options()
            letter_type = st.selectbox("편지 종류", list(letter_type_options.keys()), format_func=lambda x: letter_type_options[x])
        special_occasion = st.text_input("특별한 날 (선택사항)", placeholder="예: 100일, 생일, 발렌타인데이")
        custom_message = st.text_area("추가하고 싶은 메시지 (선택사항)", placeholder="특별히 포함하고 싶은 내용이 있다면 작성해주세요.")
        submitted = st.form_submit_button("💝 편지 작성하기", type="primary")
    if submitted:
        if not recipient_name or not sender_name or not relationship_duration:
            st.error("필수 정보를 모두 입력해주세요.")
            return
        with st.spinner("AI가 편지를 작성하고 있습니다..."):
            result = love_letter_generator.generate_love_letter(
                recipient_name=recipient_name,
                sender_name=sender_name,
                relationship_duration=relationship_duration,
                tone=tone,
                letter_type=letter_type,
                special_occasion=special_occasion if special_occasion else None,
                custom_message=custom_message if custom_message else None
            )
        if result["success"]:
            st.success("편지가 완성되었습니다! 💕")
            st.markdown("---")
            st.markdown("### 📝 생성된 편지")
            letter_style = """
            <div style="
                background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                margin: 20px 0;
                font-family: 'Nanum Gothic', sans-serif;
                line-height: 1.8;
                color: #333;
            ">
            """
            st.markdown(letter_style + result["letter"].replace('\n', '<br>') + "</div>", unsafe_allow_html=True)
            with st.expander("📋 편지 정보"):
                metadata = result["metadata"]
                st.write(f"**받는 사람:** {metadata['recipient']}")
                st.write(f"**보내는 사람:** {metadata['sender']}")
                st.write(f"**편지 톤:** {love_letter_generator.tone_styles[metadata['tone']]}")
                st.write(f"**편지 종류:** {love_letter_generator.letter_types[metadata['type']]}")
                st.write(f"**연애 기간:** {metadata['relationship_duration']}")
            if st.button("📋 편지 복사하기"):
                st.write("편지 내용이 클립보드에 복사되었습니다!")
                st.code(result["letter"])
        else:
            st.error(f"편지 생성에 실패했습니다: {result['error']}")

def show_resume_generator():
    st.title("📄 한류 스타일 이력서 생성기")
    st.info("🚧 개발 중인 기능입니다. 곧 만나보실 수 있습니다!")

def show_midjourney_helper():
    st.title("🎨 미드저니 프롬프트 도우미")
    st.info("🚧 개발 중인 기능입니다. 곧 만나보실 수 있습니다!")

def show_tiktok_generator():
    st.title("📱 틱톡 자막 생성기")
    st.info("🚧 개발 중인 기능입니다. 곧 만나보실 수 있습니다!")

def show_drama_generator():
    st.title("🎭 드라마 대사 생성기")
    st.info("🚧 개발 중인 기능입니다. 곧 만나보실 수 있습니다!")

if __name__ == "__main__":
    main() 