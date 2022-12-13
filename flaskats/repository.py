from abc import ABC, abstractmethod
from flask import request
import requests
import json

from flaskats import Config
from flaskats.dto import Application

class Repository(ABC):

    @abstractmethod
    def list_records():
        return

    @abstractmethod
    def create_record():
        return
        
    @abstractmethod
    def update_notified_records(dtos):
        return

class AirtableRepository(Repository):
    
    # repository URLs class variables
    bases_url = 'https://api.airtable.com/v0/meta/bases'
    records_url = f"https://api.airtable.com/v0/{Config.BASE_ID}/{Config.TABLE_NAME}"

    headers = {'accept': 'application/json', 
                'content-type': 'application/json',
                'Authorization': f"Bearer {Config.REPOSITORY_TOKEN}" }

    def create_record(self, app: Application): 
        r = requests.post(
                        self.records_url,
                        headers = self.headers,
                        json = {"fields":  app.to_dict() }
                    )
        return r.json()  

    def list_records(self, params={}):
        r = requests.get(
                        self.records_url,
                        headers = self.headers,
                        params = params
                    )
        return r.json()  

    def _create_json_update(self, dtos):
        data_dict =  { "records": [] }
        
        for id, dto in dtos.items():
            data = { 'fields': dto,
                     'id': id }
            data_dict["records"].append(data)
        return data_dict
        
    
    def update_notified_records(self, dtos):        
        r = requests.patch(
                        self.records_url,
                        headers = self.headers,
                        json = self._create_json_update(dtos)
                    )
        print(r.json())
        return r.json()


        