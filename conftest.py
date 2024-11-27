import pytest

@pytest.fixture()
def b_a():
    print('\nbefore')
    yield
    print('\nafter')