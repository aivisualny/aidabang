"""
aidabang 설정 관리
"""
import os
from typing import Optional
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings:
    """애플리케이션 설정 클래스"""
    
    # 앱 기본 설정
    APP_NAME: str = "aidabang"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # API 키들
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    MIDJOURNEY_API_KEY: Optional[str] = os.getenv("MIDJOURNEY_API_KEY")
    DALLE_API_KEY: Optional[str] = os.getenv("DALLE_API_KEY")
    
    # 로깅 설정
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # 데이터베이스 설정
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///aidabang.db")
    
    @classmethod
    def validate_api_keys(cls) -> bool:
        """필수 API 키들이 설정되어 있는지 확인"""
        required_keys = ["OPENAI_API_KEY"]
        missing_keys = [key for key in required_keys if not getattr(cls, key)]
        
        if missing_keys:
            print(f"⚠️  경고: 다음 API 키들이 설정되지 않았습니다: {', '.join(missing_keys)}")
            return False
        return True

# 전역 설정 인스턴스
settings = Settings() 