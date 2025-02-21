import os
from dotenv import load_dotenv

def test_env_loading():
    """测试环境变量加载"""
    load_dotenv()
    assert os.getenv('API_KEYS') is not None
    assert os.getenv('BASE_URL') is not None 