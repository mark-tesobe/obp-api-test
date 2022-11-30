from typing import Any

import requests

# BASE_URI = "http://127.0.0.1:8080"  # TODO: move to .env
BASE_URI = "https://test.openbankproject.com"
VERSION = "v5.0.0"  # TODO: move to .env

# PATHS
SWAGGER_PATH = f"/obp/{VERSION}/resource-docs/{VERSION}/swagger"
BANK_ID = "Mobilink"


def absolute_uri(path: str) -> str:
    return BASE_URI + path


def load_swagger() -> Any:
    uri = absolute_uri(SWAGGER_PATH)
    request = requests.get(uri)
    return request.json()
