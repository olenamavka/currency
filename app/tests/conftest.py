import pytest
# from django.core.management import call_command
from rest_framework.test import APIClient
from account.models import User
from model_bakery import baker


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


@pytest.fixture()
def api_client():
    client = APIClient()
    yield client


# @pytest.fixture(autouse=True, scope="session")
# def load_fixtures(django_db_setup, django_db_blocker):
#     with django_db_blocker.unblock():
#         fixtures = (
#             'sources.json',
#             'rates.json',
#         )
#         for fixture in fixtures:
#             call_command('loaddata', f'app/tests/fixtures/{fixture}')


@pytest.fixture()
def auth_client(api_client):
    user = User.objects.create_user(username="test_user")
    api_client.force_authenticate(user)
    yield api_client


@pytest.fixture
def test_source():
    source = baker.make('currency.Source')
    return source
