import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import myproject.mymodule as mym
import pytest

# pytest --cov=myproject tests/

def test_func1():
    assert mym.func1(2) == 3

def test_mygreetings():
    testname = "Joe" # Arrange
    testgreetings = mym.mygreetings(testname) # Act
    assert testgreetings == "Hello Joe" # Assert

@pytest.mark.parametrize(
    "a, expected",
    [
        ([1, 2, 4], 7),
        ([1, 1, 2], 4),
        ([-2, 0, 2], 0)
    ]
)
def test_myfunc1(a, expected):
    # test_sum = myfunc1(get_data)
    assert mym.myfunc1(a) == expected

def test_myfunc2(get_data):
    test_len = mym.myfunc2(get_data)
    assert test_len == len(range(5))



print("----------- test_mymodule executed --------------")
