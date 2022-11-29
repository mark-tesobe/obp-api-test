import obp_python

# Configure API key authorization: directLogin
configuration = obp_python.Configuration()
# configuration.api_key['Authorization'] = 'Bearer n2qiswa1stx2l3gagaxnvpmpghohl4eg4al5w55m'
# configuration.api_key['Authorization'] = 'Bearer rm0vmduxqryj3lbq1t51dvfpbyufv41jgtcvxqs1'

# create an instance of the API class
api_instance = obp_python.BankApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson("")
api_version = "v5.0.0"  # str | eg:v2.2.0, v3.0.0
bank_id = "Mobilink"  # str | The bank id


def test_transaction_types() -> None:
    api_response = api_instance.o_bpv2_0_0_get_transaction_types(
        body, bank_id
    ).to_dict()
    assert type(api_response) is dict
    assert "transaction_types" in api_response
    assert len(api_response["transaction_types"]) == 0
