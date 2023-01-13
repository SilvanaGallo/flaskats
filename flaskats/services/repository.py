from abc import ABC, abstractmethod
import requests
from flaskats import Config
from flaskats.dtos import Application
from flaskats.models import ApplicationStatus
from flaskats.repositories import SQLAlchemyOffersRepository


class Repository(ABC):

    @abstractmethod
    def list_records(self):
        return

    @abstractmethod
    def create_record(self, app: Application):
        return

    @abstractmethod
    def update_notified_records(self, dtos):
        return


class RecruiteeRepository(Repository):

    def __init__(self):
        self.offers_repository = SQLAlchemyOffersRepository()

    # repository URLs class variables
    candidates_url = f"https://api.recruitee.com/c/{Config.COMPANY_ID}/candidates"
    update_url = f"https://api.recruitee.com/c/{Config.COMPANY_ID}/bulk/candidates/tags"
    headers = {'accept': 'application/json',
               'authorization': f"Bearer {Config.RECRUITEE_TOKEN}"}

    def _create_dictionary(self, response) -> dict:
        response_dict: dict = {'records': []}
        for app in response['candidates']:

            for job in app["placements"]:
                job_code: int = self.offers_repository.get_offer_by_repository_id(job['offer_id']).code

                app_dict: dict = {
                                'name': app["name"],
                                'email': app['emails'][0],
                                'job': job_code,
                                'date': job['created_at'],
                                'candidate_id': job['candidate_id']
                            }

                if 'disqualify_reason' in job:
                    app_dict['status'] = ApplicationStatus.REJECTED
                else:
                    if job['hired_at'] is not None:
                        app_dict['status'] = ApplicationStatus.HIRED

                app_dto = Application.from_dict(app_dict)
                app_dto.notified = self.get_notified(app_dto)

                response_dict['records'].append(app_dto)
        return response_dict

    def list_records(self, params=None):
        if params is None:
            params = {}
        response = requests.get(
                        self.candidates_url,
                        headers=self.headers,
                        params=params
                    )
        response = self._create_dictionary(response.json())

        return response

    def create_record(self, app: Application):
        response = requests.post(
                        self.candidates_url,
                        headers=self.headers,
                        json={
                            "candidate": {
                                "emails": [app.email],
                                "name": app.name
                            },
                            "offers": [app.job]}
                    )
        return response.json()

    def _create_json_update(self, dtos):
        data_dict = {"candidates": []}
        for item_id, dto in dtos.items():
            data_dict["candidates"].append(item_id)
        data_dict["tags"] = ["notified"]
        return data_dict

    def update_notified_records(self, dtos):
        response = requests.patch(
                        self.update_url,
                        headers=self.headers,
                        json=self._create_json_update(dtos)
                    )
        return response.json()

    def get_candidate(self, app_dto):
        url = f"{self.candidates_url}/{app_dto.candidate_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def get_notified(self, app_dto) -> bool:
        response = self.get_candidate(app_dto)
        response = response.json()
        return "notified" in response["candidate"]["tags"]


class AirtableRepository(Repository):

    # repository URLs class variables
    bases_url = 'https://api.airtable.com/v0/meta/bases'
    records_url = f"https://api.airtable.com/v0/{Config.BASE_ID}/{Config.TABLE_NAME}"

    headers = {'accept': 'application/json',
               'content-type': 'application/json',
               'Authorization': f"Bearer {Config.REPOSITORY_TOKEN}"}

    def create_record(self, app: Application):
        response = requests.post(
                        self.records_url,
                        headers=self.headers,
                        json={"fields":  app.to_dict()}
                    )
        return response.json()

    def list_records(self, params=None):
        if params is None:
            params = {}
        response = requests.get(
                        self.records_url,
                        headers=self.headers,
                        params=params
                    )
        return response.json()

    def _create_json_update(self, dtos):
        data_dict = {"records": []}
        print(dtos)
        for item_id, dto in dtos.items():
            data = {'fields': dto,
                    'id': item_id}
            data_dict["records"].append(data)
        return data_dict

    def update_notified_records(self, dtos):
        response = requests.patch(
                        self.records_url,
                        headers=self.headers,
                        json=self._create_json_update(dtos)
                    )
        return response.json()
