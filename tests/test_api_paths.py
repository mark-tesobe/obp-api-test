from typing import Any, Dict, List

import pytest
from requests import Session

from conftest import Path
from settings import API_PATH_URI as path_uri
from settings import URI_BASE_PATH as base_path
from settings import absolute_uri


@pytest.fixture(scope="module")
def api_paths(paths: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filter all OBP endpoints under the `/bank` path."""

    prefix_path = base_path + path_uri
    return [items for items in paths for path in items if path.startswith(prefix_path)]


def test_paths(api_paths: Any, http_session: Session) -> None:
    """Test all OBP bank paths."""

    for items in api_paths:
        for path, details in items.items():
            _test_get_methods(path, details, http_session)
    print(f"GET requests at {absolute_uri(path_uri,True)}/* are completed.")


def _test_get_methods(
    path: Any, path_details: List[Path], http_session: Session
) -> None:
    """Test all OBP bank paths with `GET` method."""

    for detail in path_details:
        if detail.method == "get":
            uri = absolute_uri(path)
            response = http_session.get(uri)
            print(f"\t{uri} : {response.status_code}")
            assert response.status_code == 200
