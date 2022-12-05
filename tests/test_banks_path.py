from typing import List, Tuple

import pytest
from requests import Session

from conftest import Path
from settings import BANK_PATH_URI as path_uri
from settings import absolute_uri

BANK_ID_QUERY_STRING_PARAMETER = "{BANK_ID}"


@pytest.mark.parametrize("sub_paths", [path_uri], indirect=["sub_paths"])
def test_banks_get_methods(
    sub_paths: List[Tuple[str, List[Path]]],
    default_bank_id: str,
    http_session: Session,
) -> None:
    """Test all OBP /banks paths with `GET` method."""

    for path, details in sub_paths:
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
