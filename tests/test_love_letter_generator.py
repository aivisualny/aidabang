"""
AI 연애편지 작성기 테스트
"""
import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# 프로젝트 루트를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.tools.love_letter_generator import LoveLetterGenerator

class TestLoveLetterGenerator(unittest.TestCase):
    """AI 연애편지 작성기 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.generator = LoveLetterGenerator()
    
    def test_initialization(self):
        """초기화 테스트"""
        self.assertIsNotNone(self.generator.tone_styles)
        self.assertIsNotNone(self.generator.letter_types)
        self.assertIn("romantic", self.generator.tone_styles)
        self.assertIn("daily", self.generator.letter_types)
    
    def test_get_tone_options(self):
        """톤 옵션 반환 테스트"""
        options = self.generator.get_tone_options()
        self.assertIsInstance(options, dict)
        self.assertIn("romantic", options)
        self.assertIn("cute", options)
        self.assertIn("mature", options)
    
    def test_get_letter_type_options(self):
        """편지 타입 옵션 반환 테스트"""
        options = self.generator.get_letter_type_options()
        self.assertIsInstance(options, dict)
        self.assertIn("confession", options)
        self.assertIn("daily", options)
        self.assertIn("anniversary", options)
    
    def test_build_prompt(self):
        """프롬프트 구성 테스트"""
        prompt = self.generator._build_prompt(
            recipient_name="민수",
            sender_name="영희",
            relationship_duration="1년",
            tone="romantic",
            letter_type="daily",
            special_occasion=None,
            custom_message=None
        )
        
        self.assertIsInstance(prompt, str)
        self.assertIn("민수", prompt)
        self.assertIn("영희", prompt)
        self.assertIn("1년", prompt)
        self.assertIn("로맨틱하고 감성적인", prompt)
    
    @patch('src.utils.ai_client.ai_client.generate_text_with_openai')
    def test_generate_love_letter_success(self, mock_generate):
        """편지 생성 성공 테스트"""
        # Mock 설정
        mock_generate.return_value = "사랑하는 민수에게..."
        
        result = self.generator.generate_love_letter(
            recipient_name="민수",
            sender_name="영희",
            relationship_duration="1년"
        )
        
        self.assertTrue(result["success"])
        self.assertIn("letter", result)
        self.assertIn("metadata", result)
        self.assertEqual(result["metadata"]["recipient"], "민수")
        self.assertEqual(result["metadata"]["sender"], "영희")
    
    @patch('src.utils.ai_client.ai_client.generate_text_with_openai')
    def test_generate_love_letter_failure(self, mock_generate):
        """편지 생성 실패 테스트"""
        # Mock 설정 - None 반환
        mock_generate.return_value = None
        
        result = self.generator.generate_love_letter(
            recipient_name="민수",
            sender_name="영희",
            relationship_duration="1년"
        )
        
        self.assertFalse(result["success"])
        self.assertIn("error", result)
    
    @patch('src.utils.ai_client.ai_client.generate_text_with_openai')
    def test_invalid_tone_and_type(self, mock_generate):
        """잘못된 톤과 타입 처리 테스트"""
        # Mock 설정
        mock_generate.return_value = "사랑하는 민수에게..."
        
        result = self.generator.generate_love_letter(
            recipient_name="민수",
            sender_name="영희",
            relationship_duration="1년",
            tone="invalid_tone",
            letter_type="invalid_type"
        )
        
        # 기본값으로 설정되어야 함
        self.assertEqual(result["metadata"]["tone"], "romantic")
        self.assertEqual(result["metadata"]["type"], "daily")

if __name__ == "__main__":
    unittest.main() 