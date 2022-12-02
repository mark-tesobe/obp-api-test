import pytest
from obp_python import APIApi, ApiClient, Configuration, EmptyClassJson

from settings import TARGET_DEFAULT_SDK_BANK_ID as default_bank_id
from settings import VERSION


@pytest.fixture(scope="module")
def obp_api(sdk_obp_python_configuration: Configuration) -> APIApi:
    """Creates an OBP APIApi instance."""

    return APIApi(ApiClient(sdk_obp_python_configuration))


def test_api_docs(sdk_obp_bank_default_body: EmptyClassJson, obp_api: APIApi) -> None:
    """Test OBP SDK API docs"""

    api_response = obp_api.o_bpv1_4_0_get_bank_level_dynamic_resource_docs_obp(
        sdk_obp_bank_default_body, VERSION, default_bank_id
    ).to_dict()
    print(api_response)
    assert type(api_response) is dict
    assert "meta" in api_response
    assert "resource_docs" in api_response
    assert len(api_response["resource_docs"]) == 0
