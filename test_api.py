# test_api.py
# API-level automated tests (no browser) using requests + pytest,
# targeting the public reqres.in test API.
#
# This complements the UI tests (test_login.py, test_cart_checkout.py) by
# validating backend behavior directly — status codes, response structure,
# and error handling — rather than through a browser.

import requests
import pytest

BASE_URL = "https://reqres.in/api"
HEADERS = {"x-api-key": "reqres-free-v1"}  # required by reqres.in's free tier


def test_get_single_user_returns_200_and_correct_id():
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)

    assert response.status_code == 200
    body = response.json()
    assert body["data"]["id"] == 2
    assert "email" in body["data"]


def test_get_nonexistent_user_returns_404():
    response = requests.get(f"{BASE_URL}/users/999", headers=HEADERS)

    assert response.status_code == 404


def test_get_users_list_returns_paginated_data():
    response = requests.get(f"{BASE_URL}/users?page=1", headers=HEADERS)

    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert isinstance(body["data"], list)
    assert body["page"] == 1


def test_create_user_returns_201_and_echoes_data():
    payload = {"name": "Ronit Golan", "job": "QA Automation Engineer"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert "id" in body
    assert "createdAt" in body


def test_update_user_returns_200_and_updated_job():
    payload = {"name": "Ronit Golan", "job": "Senior QA Automation Engineer"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=HEADERS)

    assert response.status_code == 200
    body = response.json()
    assert body["job"] == "Senior QA Automation Engineer"
    assert "updatedAt" in body


def test_delete_user_returns_204():
    response = requests.delete(f"{BASE_URL}/users/2", headers=HEADERS)

    assert response.status_code == 204


def test_register_without_password_returns_400_with_error_message():
    payload = {"email": "sydney@fife"}
    response = requests.post(f"{BASE_URL}/register", json=payload, headers=HEADERS)

    assert response.status_code == 400
    body = response.json()
    assert "error" in body
