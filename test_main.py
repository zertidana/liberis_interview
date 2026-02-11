"""Test script for main.py."""
import requests
from main import api


def test_api_returns_200_status_code(fake_api):
    response = fake_api.get("/revenue")
    assert response.status_code == 200
    assert response.json[0] == {"total_revenue": 0}


def test_api_post_returns_valid_success_code(fake_api, fake_data):
    response = fake_api.post("/revenue", json=fake_data)
    assert response.status_code == 201