import pytest

import requests
from rest_framework import status

# @pytest.fixture()
# def setup():
#     client = APIClient()
#     return client


def test_account_login():
    payload = {'email': 'admin@gmail.com', 'password': '1'}
    res = requests.post("http://localhost:8000/api/account/login/", payload)
    assert res.status_code == 200


def test_account_register():
    payload = {'name': 'Akobir', 'email': 'akobir123@gmail.com', 'role': 'customer', 'password': 'Mr_coolman_23'}
    resp = requests.post("http://localhost:8000/api/account/register/", payload)
    assert resp.status_code == 400


def test_account_list():
    response = requests.get("http://localhost:8000/api/account/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_account_create():
    response = requests.get("http://localhost:8000/api/account/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
