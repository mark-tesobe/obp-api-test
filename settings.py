import os
from typing import Any

import requests

TARGET_DEFAULT_BANK_ID = "THE_DEFAULT_BANK_ID"  # TODO: move to .env
TARGET_DEFAULT_SDK_BANK_ID = "whatse"  # "Mobilink"

BASE_URI = "http://127.0.0.1:8080"  # TODO: move to .env
# BASE_URI = "https://test.openbankproject.com"  # TODO: move to .env
VERSION = "v5.0.0"  # TODO: move to .env
LOGIN_AUTHORIZATION_HEADER = os.environ[
    "DIRECT_LOGIN_AUTHORIZATION_HEADER"
]  # "DirectLogin username=xxx,password=xxx,consumer_key=xxx"

# PATHS
URI_BASE_PATH = f"/obp/{VERSION}"
SWAGGER_PATH = f"{URI_BASE_PATH}/resource-docs/{VERSION}/swagger"

# /banks path
BANK_PATH_URI = "/banks"

# api path
API_PATH_URI = "/api/"

# users path
USERS_PATH_URI = "/users"

# users path
MY_PATH_URI = "/my"


def absolute_uri(path: str, use_base_path: bool = False) -> str:
    """Construct the absolute URI with a specified path."""

    return BASE_URI + URI_BASE_PATH + path if use_base_path else BASE_URI + path


def load_swagger() -> Any:
    """Get OBP swagger specifications."""

    uri = absolute_uri(SWAGGER_PATH)
    request = requests.get(uri)
    return request.json()
