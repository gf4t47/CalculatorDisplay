import pytest

from src.main import write


@pytest.mark.parametrize("num", [
    0, 1, 3, 4, 5, 6, 7, 8, 9,
    10, 77, 80, 90,
    70128,
    70056128,
    12345678901234567890
])
def test_svg(num):
    assert write(num) is not None
