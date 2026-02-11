"""Conftest file that contains all fixtures for the api tests."""

import pytest
from main import api

@pytest.fixture()
def fake_api():
    """Fake api."""
    return api.test_client()

@pytest.fixture()
def fake_data():
    """Fake data for testing."""
    return {
        "partner_id": 2,
        "merchant_id": 2,
        "total_amount": 100,
        "count_transactions": 10,
        "currency": "USD",
        "transaction": "RETURN",
        "description": "Revenue from partner 2"
    }