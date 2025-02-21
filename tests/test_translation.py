import pytest
from Segmente import MarkdownSegmenter
from pathlib import Path

@pytest.mark.asyncio(scope="session")
async def test_segmenter():
    """测试分段功能"""
    test_content = "This is a test.\n\n## Section 1\nContent here."
    test_file = Path("workmd/test.md")
    test_file.write_text(test_content)
    try:
        segmenter = MarkdownSegmenter(max_length=100)
        segments = segmenter.segment(test_content)
        assert len(segments) == 2
        assert "Section 1" in segments[1]
    finally:
        test_file.unlink(missing_ok=True) 