import pytest
from obp_python import ApiClient, Configuration, UserApi


@pytest.fixture(scope="module")
def obp_user(sdk_obp_python_configuration: Configuration) -> UserApi:
    """Creates an OBP UserApi instance."""

    return UserApi(ApiClient(sdk_obp_python_configuration))


def test_api_docs(obp_user: UserApi) -> None:
    """Test OBP SDK User"""

    pass
    # api_response = obp_user.o_bpv4_0_0_get_users().to_dict()
    # print(api_response)
    # assert type(api_response) is dict
    # assert "meta" in api_response
