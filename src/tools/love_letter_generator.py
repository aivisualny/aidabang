"""
AI 연애편지 작성기
"""
from typing import Dict, Any, Optional
from src.utils.ai_client import ai_client

class LoveLetterGenerator:
    """AI 연애편지 작성기 클래스"""
    
    def __init__(self):
        self.tone_styles = {
            "romantic": "로맨틱하고 감성적인",
            "cute": "귀엽고 사랑스러운",
            "mature": "성숙하고 진중한",
            "playful": "장난스럽고 재미있는",
            "poetic": "시적이고 문학적인"
        }
        
        self.letter_types = {
            "confession": "고백편지",
            "anniversary": "기념일편지",
            "apology": "사과편지",
            "daily": "일상편지",
            "long_distance": "원거리연애편지"
        }
    
    def generate_love_letter(
        self,
        recipient_name: str,
        sender_name: str,
        relationship_duration: str,
        tone: str = "romantic",
        letter_type: str = "daily",
        special_occasion: Optional[str] = None,
        custom_message: Optional[str] = None
    ) -> Dict[str, Any]:
        """연애편지 생성"""
        
        # 톤과 편지 타입 검증
        if tone not in self.tone_styles:
            tone = "romantic"
        if letter_type not in self.letter_types:
            letter_type = "daily"
        
        # 프롬프트 구성
        prompt = self._build_prompt(
            recipient_name=recipient_name,
            sender_name=sender_name,
            relationship_duration=relationship_duration,
            tone=tone,
            letter_type=letter_type,
            special_occasion=special_occasion,
            custom_message=custom_message
        )
        
        # AI로 편지 생성
        generated_letter = ai_client.generate_text_with_openai(
            prompt=prompt,
            model="gpt-3.5-turbo",
            max_tokens=800,
            temperature=0.8
        )
        
        if not generated_letter:
            return {
                "success": False,
                "error": "편지 생성에 실패했습니다. API 키를 확인해주세요."
            }
        
        return {
            "success": True,
            "letter": generated_letter,
            "metadata": {
                "recipient": recipient_name,
                "sender": sender_name,
                "tone": tone,
                "type": letter_type,
                "relationship_duration": relationship_duration
            }
        }
    
    def _build_prompt(
        self,
        recipient_name: str,
        sender_name: str,
        relationship_duration: str,
        tone: str,
        letter_type: str,
        special_occasion: Optional[str],
        custom_message: Optional[str]
    ) -> str:
        """프롬프트 구성"""
        
        tone_desc = self.tone_styles[tone]
        type_desc = self.letter_types[letter_type]
        
        prompt = f"""
당신은 감성적이고 로맨틱한 연애편지 작성 전문가입니다.
다음 조건에 맞는 {tone_desc} {type_desc}를 작성해주세요.

**편지 정보:**
- 받는 사람: {recipient_name}
- 보내는 사람: {sender_name}
- 연애 기간: {relationship_duration}
- 편지 톤: {tone_desc}
- 편지 종류: {type_desc}
"""

        if special_occasion:
            prompt += f"- 특별한 날: {special_occasion}\n"
        
        if custom_message:
            prompt += f"- 추가하고 싶은 메시지: {custom_message}\n"
        
        prompt += """
**요구사항:**
1. 한국어로 자연스럽게 작성
2. 감정이 진실하고 진심이 담긴 내용
3. 구체적인 추억이나 일화 포함
4. 미래에 대한 기대나 약속 포함
5. 적절한 줄바꿈과 문단 구분
6. 300-500자 내외로 작성

편지만 작성하고 다른 설명은 하지 마세요.
"""
        
        return prompt
    
    def get_tone_options(self) -> Dict[str, str]:
        """사용 가능한 톤 옵션 반환"""
        return self.tone_styles.copy()
    
    def get_letter_type_options(self) -> Dict[str, str]:
        """사용 가능한 편지 타입 옵션 반환"""
        return self.letter_types.copy()

# 전역 인스턴스
love_letter_generator = LoveLetterGenerator() 