import pytest

@pytest.fixture
def get_data():
    return list(range(5))
