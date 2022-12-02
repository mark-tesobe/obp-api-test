import pytest
from obp_python import ApiClient, BankApi, Configuration, EmptyClassJson

from settings import TARGET_DEFAULT_SDK_BANK_ID as default_bank_id


@pytest.fixture(scope="module")
def obp_bank_api(sdk_obp_python_configuration: Configuration) -> BankApi:
    """Creates an OBP BankApi instance."""

    return BankApi(ApiClient(sdk_obp_python_configuration))


def test_transaction_types(
    sdk_obp_bank_default_body: EmptyClassJson, obp_bank_api: BankApi
) -> None:
    """Test OBP SDK transaction types"""

    api_response = obp_bank_api.o_bpv2_0_0_get_transaction_types(
        sdk_obp_bank_default_body, default_bank_id
    ).to_dict()
    print(api_response)
    assert type(api_response) is dict
    assert "transaction_types" in api_response
    assert len(api_response["transaction_types"]) == 0


def test_get_bank(obp_bank_api: BankApi) -> None:
    """Test OBP SDK banks"""

    api_response = obp_bank_api.o_bpv5_0_0_get_bank(default_bank_id).to_dict()
    print(api_response)
    assert type(api_response) is dict
    # assert "transaction_types" in api_response
    # assert len(api_response["transaction_types"]) == 0
