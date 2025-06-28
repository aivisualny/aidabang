"""
AI API 클라이언트 관리
"""
import openai
import anthropic
from typing import Optional, Dict, Any
from src.config.settings import settings

class AIClient:
    """AI API 클라이언트 관리 클래스"""
    
    def __init__(self):
        self.openai_client = None
        self.anthropic_client = None
        self._initialize_clients()
    
    def _initialize_clients(self):
        """API 클라이언트 초기화"""
        if settings.OPENAI_API_KEY:
            self.openai_client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        
        if settings.ANTHROPIC_API_KEY:
            self.anthropic_client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    
    def generate_text_with_openai(
        self, 
        prompt: str, 
        model: str = "gpt-3.5-turbo",
        max_tokens: int = 1000,
        temperature: float = 0.7
    ) -> Optional[str]:
        """OpenAI API를 사용하여 텍스트 생성"""
        if not self.openai_client:
            raise ValueError("OpenAI API 키가 설정되지 않았습니다.")
        
        try:
            response = self.openai_client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI API 오류: {e}")
            return None
    
    def generate_text_with_claude(
        self,
        prompt: str,
        model: str = "claude-3-sonnet-20240229",
        max_tokens: int = 1000
    ) -> Optional[str]:
        """Claude API를 사용하여 텍스트 생성"""
        if not self.anthropic_client:
            raise ValueError("Anthropic API 키가 설정되지 않았습니다.")
        
        try:
            response = self.anthropic_client.messages.create(
                model=model,
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            print(f"Claude API 오류: {e}")
            return None
    
    def generate_image_with_dalle(
        self,
        prompt: str,
        size: str = "1024x1024",
        quality: str = "standard",
        n: int = 1
    ) -> Optional[list]:
        """DALL-E API를 사용하여 이미지 생성"""
        if not self.openai_client:
            raise ValueError("OpenAI API 키가 설정되지 않았습니다.")
        
        try:
            response = self.openai_client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size=size,
                quality=quality,
                n=n
            )
            return [image.url for image in response.data]
        except Exception as e:
            print(f"DALL-E API 오류: {e}")
            return None

# 전역 AI 클라이언트 인스턴스
ai_client = AIClient() 