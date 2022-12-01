from typing import Any, Dict, List

import pytest
from requests import Session

from conftest import Path
from settings import TARGET_DEFAULT_BANK_ID as target_default_bank_id
from settings import URI_BASE_PATH as base_path
from settings import absolute_uri

BANK_PATH_URI = "/banks"
BANK_ID_QUERY_STRING_PARAMETER = "{BANK_ID}"


@pytest.fixture(scope="module")
def bank_paths(paths: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filter all OBP endpoints under the `/bank` path."""

    prefix_path = f"{base_path}/bank"
    return [items for items in paths for path in items if path.startswith(prefix_path)]


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


def test_paths(bank_paths: Any, default_bank_id: str, http_session: Session) -> None:
    """Test all OBP bank paths."""

    for items in bank_paths:
        for path, details in items.items():
            _test_get_methods(path, details, default_bank_id, http_session)
    print(f"GET requests at {absolute_uri(BANK_PATH_URI,True)}/* are completed.")


def _test_get_methods(
    path: Any, path_details: List[Path], default_bank_id: str, http_session: Session
) -> None:
    """Test all OBP bank paths with `GET` method."""

    for detail in path_details:
        # if detail.method == "get"
        #    and "Account-Public" in  detail.tags
        #    or "PublicData" in detail.tags
        #    and "{" not in path:
        path_length = path.count("/")
        if (
            detail.method == "get" and path_length <= 5
        ):  # For now just test paths that rquires BANK_ID only.
            uri = absolute_uri(path).replace(
                BANK_ID_QUERY_STRING_PARAMETER, default_bank_id
            )
            response = http_session.get(uri)
            print(f"\t{uri} : {response.status_code}")
            # print(f"{path} : {response.status_code}")
            # assert request.status_code == 200
