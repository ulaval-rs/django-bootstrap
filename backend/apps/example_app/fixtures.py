# test fixtures go here
import pytest

# Fixtures return a function that can be passed as a parameter to a test (see tests.py)
# Fixtures must be referenced in backend/conftest.py to be available to all tests


@pytest.fixture(scope="function")
def my_fixture():
    def function():
        pass

    return function
