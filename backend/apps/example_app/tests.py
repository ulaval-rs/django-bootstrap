# tests go here
import pytest


@pytest.mark.django_db()
def test_empty(client, my_fixture):
    # The fixture my_fixture is defined in fixtures.py
    pass
