# import os.path
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# import myproject.mymodule1 as mym1


import myproject.mymodule1 as mym1
import pytest

# python -m pytest -v --cov=myproject --cov-report html tests/
# python -m pytest -v --cov=myproject tests/
# xdg-open htmlcov/index.html

def test_func1():
    assert mym1.func1(2) == 3

def test_mygreetings():
    testname = "Joe" # Arrange
    testgreetings = mym1.mygreetings(testname) # Act
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
    assert mym1.myfunc1(a) == expected

def test_myfunc2(get_data):
    test_len = mym1.myfunc2(get_data)
    assert test_len == len(range(5))

# git init
# git status
# git branch my_branch
# git branch -v
# git checkout my_branch
# git add .
# git commit -m "expain commmit"
# git push origin my_branch

# git checkout main
# git merge my_branch
# git remote show origin
