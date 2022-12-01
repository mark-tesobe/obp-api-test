from obp_python import BankApi, EmptyClassJson

from settings import TARGET_DEFAULT_BANK_ID


def test_transaction_types(
    obp_bank_default_body: EmptyClassJson, obp_bank_api: BankApi
) -> None:
    """OBP SDK transaction types"""
    api_response = obp_bank_api.o_bpv2_0_0_get_transaction_types(
        obp_bank_default_body, TARGET_DEFAULT_BANK_ID
    ).to_dict()
    assert type(api_response) is dict
    assert "transaction_types" in api_response
    assert len(api_response["transaction_types"]) == 0
