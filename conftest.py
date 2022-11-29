from typing import List

import pytest

from settings import load_swagger


@pytest.fixture(scope="session")
def paths() -> List[str]:
    swagger = load_swagger()
    return [path for path in swagger["paths"]]
