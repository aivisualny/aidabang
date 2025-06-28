#!/usr/bin/env python3
"""
aidabang 테스트 실행 스크립트
"""
import unittest
import sys
import os

def run_tests():
    """모든 테스트 실행"""
    # 프로젝트 루트를 Python 경로에 추가
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, project_root)
    
    # 테스트 디렉토리에서 테스트 검색
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    
    # 테스트 실행
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # 결과 반환
    return result.wasSuccessful()

if __name__ == "__main__":
    print("🧪 aidabang 테스트 실행 중...")
    success = run_tests()
    
    if success:
        print("\n✅ 모든 테스트가 성공적으로 통과했습니다!")
        sys.exit(0)
    else:
        print("\n❌ 일부 테스트가 실패했습니다.")
        sys.exit(1) 