import pytest
from flaskats.services import ContractSender, HelloSignContractSender
from flaskats.dtos import Application


class TestContractSender:

    @pytest.mark.unit
    def test_contract_sender_creation(self):
        with pytest.raises(Exception):
            cs: ContractSender = ContractSender()

    @pytest.mark.unit
    def test_send_contract_abstract_method(self, mocker):
        with pytest.raises(NotImplementedError):
            mocker.patch.multiple(ContractSender, __abstractmethods__=set())
            cs: ContractSender = ContractSender()
            app_dto: Application = Application(name="AName AndSurname", email="mail@gmail.com", job="ABC-123", candidate_id=123)
            cs.send_contract(app_dto)


class TestHelloSignContractSender:

    SEND_RESPONSE = '''{
    "signature_request": {
        "signature_request_id": "97588b54e311184065a5a4a0715b754edfdd78a7",
        "test_mode": true,
        "title": "ATS App - Contract to sign",
        "original_title": "ATS App - Contract to sign",
        "subject": "ATS App - Contract to sign",
        "message": "Congratulations! We are happy to inform you that you have been selected to join the team! You were selected over many other applicants because of the skills, experience, and attitude that you will bring to the company. Please sign your contract.",
        "metadata": {},
        "created_at": 1673363161,
        "is_complete": false,
        "is_declined": false,
        "has_error": false,
        "custom_fields": [],
        "response_data": [],
        "signing_url": "https://app.hellosign.com/sign/97588b54e311184065a5a4a0715b754edfdd78a7",
        "signing_redirect_url": null,
        "final_copy_uri": "/v3/signature_request/final_copy/97588b54e311184065a5a4a0715b754edfdd78a7",
        "files_url": "https://api.hellosign.com/v3/signature_request/files/97588b54e311184065a5a4a0715b754edfdd78a7",
        "details_url": "https://app.hellosign.com/home/manage?guid=97588b54e311184065a5a4a0715b754edfdd78a7",
        "requester_email_address": "silvana.lis.g@gmail.com",
        "signatures": [
            {
                "signature_id": "211e363a72df1cfc022d47a501527879",
                "has_pin": false,
                "has_sms_auth": false,
                "has_sms_delivery": false,
                "sms_phone_number": null,
                "signer_email_address": "silvana.lis.g@hotmail.com",
                "signer_name": "Silvana",
                "signer_role": null,
                "order": null,
                "status_code": "awaiting_signature",
                "signed_at": null,
                "last_viewed_at": null,
                "last_reminded_at": null,
                "error": null
            }
        ],
        "cc_email_addresses": [],
        "template_ids": null
    },
    "warnings": [
        {
            "warning_msg": "You must upgrade your plan to use date_format",
            "warning_name": "need_credit"
        }
    ]
}'''

    @pytest.mark.unit
    def test__construct_payload(self):
        app_dto: Application = Application(name="Silvana", email="silvana.lis.g@hotmail.com", job="ABC-123", candidate_id=123)
        contract_sender: HelloSignContractSender = HelloSignContractSender()
        result: dict = contract_sender._construct_payload(app_dto=app_dto)

        signer: dict = result["signers"][0]
        assert signer["name"] == app_dto.name
        assert signer["email_address"] == app_dto.email

    @pytest.mark.unit
    def test_send_contract(self, requests_mock):
        requests_mock.post(HelloSignContractSender.sender_url, text=self.SEND_RESPONSE)

        subject = HelloSignContractSender()
        app_dto: Application = Application(name="Silvana", email="silvana.lis.g@hotmail.com", job="ABC-123", candidate_id=123)

        response = subject.send_contract(app_dto)
        print(response)

        first_signer: dict = response["signature_request"]["signatures"][0]
        assert first_signer["signer_email_address"] == app_dto.email
        assert first_signer["signer_name"] == app_dto.name
