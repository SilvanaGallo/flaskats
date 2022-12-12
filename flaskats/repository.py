from abc import ABC, abstractmethod
from flask import request
import requests
import json

from flaskats import Config

class Repository(ABC):

    @abstractmethod
    def list_records():
        return

    @abstractmethod
    def create_record():
        return
    
    @abstractmethod
    def get_record(id: int):
        return
    
    @abstractmethod
    def update_record(id: int):
        return

    @abstractmethod
    def delete_record(id: int):
        return


class AirtableRepository(Repository):
    
    # repository URLs class variables
    bases_url = 'https://api.airtable.com/v0/meta/bases'
    records_url = 'https://api.airtable.com/v0/'



    def list_records(self):
        params = request.args.to_dict()
        r = requests.get(
                        self.records_url,
                        headers = {'accept': 'application/json', 
                                    'X-Rollbar-Access-Token': Config.REPOSITORY_TOKEN},
                        params = params
                    )
        return r.json()
    
    
    # It needs a refactorization
    def _create_dictionary(self) -> dict:

        message: dict = {}
        params = request.get_json()
                
        message = {"body": params['message-body']} if "message-body" in params else {}
        message["route"] = params['route'] if "route" in params else ''
        
        payload =  {"data": {
                            "body": {
                                    "message": message
                                    }
                            }
                    }

        for i in ['level', 'title', 'user-id', 'status', 'environment']:
            if i in params:
                payload["data"][i] = params[i] 
        
        return payload


    def create_record(self):
                
        r = requests.post(
                        self.record_url,
                        headers = {'accept': 'application/json', 
                                    'content-type': 'application/json', 
                                    'X-Rollbar-Access-Token': Config.POST_SERVER_record
                                },
                        json = self._create_dictionary()
                    )
        return r.json()
    

    def get_record(self, id: int):
        
        url_and_id = f"{self.record_url}/{id}" 
       
        r = requests.get(
                        url_and_id,
                        headers = {'accept': 'application/json', 
                                    'content-type': 'application/json', 
                                    'X-Rollbar-Access-Token': Config.READ},
                    )
        return r.json()
    

    def update_record(self, id: int):
        
        url_and_id = f"{self.record_url}/{id}" 
        data_dict =  request.get_json()
        
        r = requests.patch(
                        url_and_id,
                        headers = {'accept': 'application/json', 
                                    'content-type': 'application/json', 
                                    'X-Rollbar-Access-Token': Config.WRITE},
                        json = data_dict
                    )
        return r.json()


    def delete_record(self, id: int):
        result = {"data": {"err": 1, "message": "records can't be deleted."}}
        return json.dumps(result, indent=2)

    
    def top_active_records(self):
    
        full_url = f"{self.reports_url}top_active_records" 
        params = request.args.to_dict()
        r = requests.get(
                        full_url,
                        headers = {'accept': 'application/json', 
                                    'content-type': 'application/json', 
                                    'X-Rollbar-Access-Token': Config.READ},
                        params=params
                    )
        return r.json()
        