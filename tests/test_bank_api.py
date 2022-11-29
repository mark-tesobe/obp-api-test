from typing import Any

import requests

from settings import VERSION as api_version
from settings import absolute_uri


def test_api(paths: Any) -> None:
    for path in paths:
        if path in [
            f"/obp/{api_version}/api/versions",
            f"/obp/{api_version}/banks",
            f"/obp/{api_version}/accounts/public",
        ]:
            # print(request.json())
            uri = absolute_uri(path)
            request = requests.get(uri)
            assert request.status_code == 200
