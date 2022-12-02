from typing import Any, Dict, List, Tuple

import pytest
from requests import Session

from conftest import Path
from settings import BANK_PATH_URI as path_uri
from settings import URI_BASE_PATH as base_path
from settings import absolute_uri

BANK_ID_QUERY_STRING_PARAMETER = "{BANK_ID}"


@pytest.fixture(scope="module")
def banks_path(paths: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filter all OBP endpoints under the `/banks` path."""

    prefix_path = base_path + path_uri
    return [items for items in paths for path in items if path.startswith(prefix_path)]


@pytest.fixture(scope="function")
def banks_path_details(banks_path: Any) -> List[Tuple[str, List[Path]]]:
    """Test all OBP /banks paths."""

    return [
        (path, details) for items in banks_path for (path, details) in items.items()
    ]


def test_banks_get_methods(
    banks_path_details: List[Tuple[str, List[Path]]],
    default_bank_id: str,
    http_session: Session,
) -> None:
    """Test all OBP /banks paths with `GET` method."""

    for path, details in banks_path_details:
        for detail in details:
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
    print(f"GET requests at {absolute_uri(path_uri,True)}/* are completed.")
