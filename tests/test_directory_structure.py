from pathlib import Path

def test_directory_structure():
    """验证必要目录结构"""
    assert Path("workmd").exists()
    assert Path("outputmd").exists()
    assert Path("inputimages").exists() 