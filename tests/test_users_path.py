from typing import Any, Dict, List, Tuple

import pytest
from requests import Session

from conftest import Path
from settings import URI_BASE_PATH as base_path
from settings import USERS_PATH_URI as path_uri
from settings import absolute_uri


@pytest.fixture(scope="module")
def users_paths(paths: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filter all OBP endpoints under the `/users` path."""

    prefix_path = base_path + path_uri
    return [items for items in paths for path in items if path.startswith(prefix_path)]


@pytest.fixture(scope="function")
def users_path_details(users_paths: Any) -> List[Tuple[str, List[Path]]]:
    """Test all OBP /users paths."""

    return [
        (path, details) for items in users_paths for (path, details) in items.items()
    ]


def test_users_get_methods(
    users_path_details: List[Tuple[str, List[Path]]],
    http_session: Session,
) -> None:
    """Test all OBP /users paths with `GET` method."""

    for path, details in users_path_details:
        for detail in details:
            if detail.method == "get":
                uri = absolute_uri(path)
                response = http_session.get(uri)
                print(f"\t{uri} : {response.status_code}")
                # assert response.status_code == 200
    print(f"GET requests at {absolute_uri(path_uri,True)}/* are completed.")
