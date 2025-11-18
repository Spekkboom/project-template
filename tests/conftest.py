import pytest

@pytest.fixture
def sample_user():
    return {"name": "Test User", "email": "test@example.com"}