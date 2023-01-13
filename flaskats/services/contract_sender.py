from abc import ABC, abstractmethod
import requests
from flaskats import Config
from flaskats.dtos import Application


class ContractSender(ABC):

    @abstractmethod
    def send_contract(self, app_dto):
        return


class HelloSignContractSender(ContractSender):

    # sender URLs variable
    sender_url = f"https://{Config.HS_API_KEY}:@api.hellosign.com//v3/signature_request/send"
    headers = {'accept': 'application/json'}

    file_url = "https://www.dropbox.com/s/711oti8ak0xb7ke/contract_model.pdf?dl=0"

    def _construct_payload(self, app_dto) -> dict:
        payload: dict = {}
        payload["title"] = "ATS App - Contract to sign"
        payload["subject"] = "ATS App - Contract to sign"
        payload["message"] = '''Congratulations! We are happy to inform you that you have been selected to join the team! You were selected over many other applicants because of the skills, experience, and attitude that you will bring to the company. Please sign your contract.'''
        payload["signers"] = [{"email_address": app_dto.email,
                               "name": app_dto.name,
                               "order": 0}]
        payload["file_url"] = [self.file_url]

        payload["signing_options"] = {
                                        "draw": True,
                                        "type": True,
                                        "upload": True,
                                        "phone": False,
                                        "default_type": "draw"
                                    }
        payload["field_options"] = {"date_format": "DD - MM - YYYY"}
        payload["test_mode"] = True

        return payload

    def send_contract(self, app_dto):
        response = requests.post(
                        self.sender_url,
                        headers=self.headers,
                        json=self._construct_payload(app_dto)
                    )
        return response.json()
