from abc import ABC, abstractmethod
import requests
from flaskats import Config
from flaskats.dto import Application


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
