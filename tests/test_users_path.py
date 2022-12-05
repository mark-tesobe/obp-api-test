from typing import List, Tuple

import pytest
from requests import Session

from conftest import Path
from settings import USERS_PATH_URI as path_uri
from settings import absolute_uri


@pytest.mark.parametrize("sub_paths", [path_uri], indirect=["sub_paths"])
def test_users_get_methods(
    sub_paths: List[Tuple[str, List[Path]]],
    http_session: Session,
) -> None:
    """Test all OBP /users paths with `GET` method."""

    for path, details in sub_paths:
        for detail in details:
            if detail.method == "get":
                uri = absolute_uri(path)
                response = http_session.get(uri)
                print(f"\t{uri} : {response.status_code}")
                # assert response.status_code == 200
    print(f"GET requests at {absolute_uri(path_uri,True)}/* are completed.")
