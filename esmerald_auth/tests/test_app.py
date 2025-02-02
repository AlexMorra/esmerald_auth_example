"""
Generated by 'esmerald createproject' using Esmerald 3.1.0.
"""
import pytest
from esmerald.testclient import EsmeraldTestClient

from ..main import get_application

pytestmark = pytest.mark.anyio


def create_app():
    app = get_application()
    return app


def get_client():
    return EsmeraldTestClient(create_app())


@pytest.fixture
def client():
    return get_client()

# Add your tests here