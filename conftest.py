from typing import Any, Dict, List, Union

import obp_python
import pytest
from obp_python import BankApi, Configuration, EmptyClassJson

from settings import load_swagger

METHODS = ["get", "put", "post", "patch", "delete"]


class Path:
    """Path class definition"""

    def __init__(self, method: str, tags: List[str]):
        self.method = method
        self.tags = tags

    def __repr__(self):
        return f"<Path method:{self.method} tags:{self.tags}>"

    def __str__(self):
        return f"{self.method} | {self.tags}"


def _get_tags(paths: Any) -> Union[Any, List[str]]:
    if "tags" in paths:
        return paths["tags"]


def _get_path_definition(paths: Any) -> List[Path]:
    return [
        Path(method, _get_tags(paths[method])) for method in METHODS if method in paths
    ]


@pytest.fixture(scope="session")
def paths() -> List[Dict[str, Any]]:
    """OBP Swagger endpoints."""

    swagger = load_swagger()
    paths = swagger["paths"]
    return [{path: _get_path_definition(paths[path])} for path in paths]


@pytest.fixture(scope="session")
def obp_python_configuration() -> Configuration:
    """OBP SDK Configuration."""

    configuration = obp_python.Configuration()
    # configuration.api_key['Authorization'] = 'Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    return configuration


@pytest.fixture(scope="session")
def obp_bank_api(obp_python_configuration: Configuration) -> BankApi:
    """Creates an OBP BankApi instance."""

    return obp_python.BankApi(obp_python.ApiClient(obp_python_configuration))


@pytest.fixture(scope="session")
def obp_bank_default_body() -> EmptyClassJson:
    """Default request json body."""

    return EmptyClassJson("")
