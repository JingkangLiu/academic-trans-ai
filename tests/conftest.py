import pytest
from pathlib import Path
import time

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """创建测试需要的临时目录"""
    test_dirs = ["workmd", "outputmd", "inputimages"]
    for d in test_dirs:
        Path(d).mkdir(exist_ok=True)
    yield
    # 测试结束后清理
    for d in test_dirs:
        path = Path(d)
        if path.exists():
            # 添加重试机制
            for f in path.glob("*"):
                try:
                    f.unlink()
                except PermissionError:
                    time.sleep(0.5)  # 等待文件释放
                    f.unlink(missing_ok=True)
            try:
                path.rmdir()
            except OSError:
                pass 