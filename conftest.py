from typing import Any, Dict, List, Tuple, Union

import pytest
import requests
from obp_python import Configuration, EmptyClassJson
from requests import Session

from settings import BANK_PATH_URI
from settings import LOGIN_AUTHORIZATION_HEADER as login_header
from settings import TARGET_DEFAULT_BANK_ID as target_default_bank_id
from settings import URI_BASE_PATH, absolute_uri, load_swagger

METHODS = ["get", "put", "post", "patch", "delete"]


class Path:
    """Path class definition"""

    def __init__(self, method: str, tags: List[str]):
        self.method = method
        self.tags = tags

    def _as_str(self) -> str:
        return f"<Path method:{self.method}, tags:{self.tags}>"

    def __repr__(self) -> str:
        return self._as_str()

    def __str__(self) -> str:
        return self._as_str()


def _get_tags(paths: Any) -> Union[Any, List[str]]:
    """Auxialiary function to get swagger tags."""

    if "tags" in paths:
        return paths["tags"]
    return None


def _get_path_definition(paths: Any) -> List[Path]:
    """Auxialiary function to construct Path object based on the swagger spec."""

    return [
        Path(method, _get_tags(paths[method])) for method in METHODS if method in paths
    ]


def _direct_login(session: Session) -> None:
    """DirectLogin to get access to private endpoint."""

    login_uri = absolute_uri("/my/logins/direct")
    authorization_header = {"Authorization": login_header}
    response = session.post(login_uri, headers=authorization_header)
    token = response.json()["token"]
    token_header = {"Authorization": f"DirectLogin token={token}"}
    session.headers.update(token_header)


@pytest.fixture(scope="session")
def http_session() -> Session:
    """HTTP session with DirecLogin authorization."""

    with requests.Session() as session:
        _direct_login(session)
        return session


@pytest.fixture(scope="session")
def paths() -> List[Dict[str, Any]]:
    """OBP Swagger endpoints."""

    swagger = load_swagger()
    paths = swagger["paths"]
    return [{path: _get_path_definition(paths[path])} for path in paths]


@pytest.fixture(scope="session")
def sdk_obp_python_configuration() -> Configuration:
    """OBP SDK Configuration."""

    configuration = Configuration()
    configuration.api_key["Authorization"] = "n2qiswa1stx2l3gagaxnvpmpghohl4eg4al5w55m"
    configuration.api_key_prefix["Authorization"] = "Bearer"
    return configuration


@pytest.fixture(scope="session")
def sdk_obp_bank_default_body() -> EmptyClassJson:
    """Default request json body."""

    return EmptyClassJson("")


@pytest.fixture(scope="session")
def default_bank_id(http_session: Session) -> str:
    """Get OBP default BANK_ID."""

    uri = absolute_uri(BANK_PATH_URI, True)
    response_json = http_session.get(uri).json()
    banks = response_json["banks"]
    for bank in banks:
        if bank["id"] == target_default_bank_id:
            return str(bank["id"])
    return str(response_json["banks"][0]["id"])


@pytest.fixture(scope="function")
def sub_paths(request: Any, paths: Any) -> List[Tuple[str, List[Path]]]:
    """Get sub path URI."""

    path_uri = request.param
    prefix_path = URI_BASE_PATH + path_uri
    return [
        (path, details)
        for items in paths
        for (path, details) in items.items()
        if path.startswith(prefix_path)
    ]
