import myproject.mymodule2 as mym2
import pytest

@pytest.mark.parametrize(
    "a, expected",
    [
        (-2, "negative"),
        (-1, "negative"),
        (10000, "very big")
    ]
)
def test_complexfunc1(a, expected):
    assert mym2.complexfunc1(a) == expected
