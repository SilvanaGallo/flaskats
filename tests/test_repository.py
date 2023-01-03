import pytest

from flaskats.repository import AirtableRepository
from flaskats.dto import Application


class TestRepository:

    CREATE_RESPONSE = '''
    {
      "createdTime": "2022-09-12T21:03:48.000Z",
      "fields": {
        "name": "AName AndSurname",
        "email": "mail@gmail.com",
        "job": "ABC-123",
        "date": "2022-09-12T21:03:48.000Z",
        "status": "Inbox",
        "notified": false
      },
      "id": "rec560UJdUtocSouk"
    }
    '''

    LIST_RESPONSE = '''
    {
      "records": [
        {
          "createdTime": "2022-09-12T21:03:48.000Z",
          "fields": {
            "name": "AName AndSurname",
            "email": "mail@gmail.com",
            "job": "ABC-123",
            "date": "2022-09-12T21:03:48.000Z",
            "status": "Inbox",
            "notified": false
          },
          "id": "rec560UJdUtocSouk"
        },
        {
          "createdTime": "2022-09-12T21:03:48.000Z",
          "fields": {
            "name": "AName2 AndSurname2",
            "email": "mail2@gmail.com",
            "job": "ABC-123",
            "date": "2022-09-12T21:03:48.000Z",
            "status": "Inbox",
            "notified": false
          },
          "id": "rec3lbPRG4aVqkeOQ"
        }
      ]
    }
    '''

    UPDATE_REQUEST = '''
    '{
        "records": [
          {
          "fields": {
            "name": "AName AndSurname",
            "email": "mail@gmail.com",
            "notified": false
            },
            "id": "rec560UJdUtocSouk"
          },
          {
          "fields": {
            "name": "AName2 AndSurname2",
            "email": "mail2@gmail.com",
            "notified": false
            },
            "id": "rec3lbPRG4aVqkeOQ"
          }
        ]
      }'
    '''

    UPDATE_RESPONSE = '''
    '{
        "records": [
          {
          "fields": {
            "name": "AName AndSurname",
            "email": "mail@gmail.com",
            "notified": true
            },
            "id": "rec560UJdUtocSouk"
          },
          {
          "fields": {
            "name": "AName2 AndSurname2",
            "email": "mail2@gmail.com",
            "notified": true
            },
            "id": "rec3lbPRG4aVqkeOQ"
          }
        ]
      }'
    '''

    @pytest.mark.unit
    def test_create_record(self, requests_mock, application_dtos):
        requests_mock.post(AirtableRepository.records_url, text=self.CREATE_RESPONSE)

        repo = AirtableRepository()
        application = Application.from_dict(application_dtos["rec560UJdUtocSouk"])
        resp = repo.create_record(application)
        assert resp["id"] == "rec560UJdUtocSouk"
        assert resp["fields"]["name"] == application_dtos["rec560UJdUtocSouk"]["name"]
        assert resp["fields"]["email"] == application_dtos["rec560UJdUtocSouk"]["email"]

    @pytest.mark.unit
    def test_list_records(self, requests_mock):
        requests_mock.get(AirtableRepository.records_url, text=self.LIST_RESPONSE)

        repo = AirtableRepository()
        resp = repo.list_records()
        assert len(resp["records"]) == 2
        assert resp["records"][0]["id"] == "rec560UJdUtocSouk"

    @pytest.mark.unit
    def test__create_json_update(self, application_dtos):
        repo = AirtableRepository()
        result = repo._create_json_update(application_dtos)
        assert "records" in result
        assert len(result["records"]) == 2
        assert result["records"][0]["id"] == "rec560UJdUtocSouk"
        assert result["records"][0]["fields"] == application_dtos["rec560UJdUtocSouk"]

    @pytest.mark.unit
    def test_update_notified_records(self, requests_mock, application_dtos):
        requests_mock.patch(AirtableRepository.records_url, text=self.UPDATE_RESPONSE)

        repo = AirtableRepository()
        resp = repo.update_notified_records(application_dtos)

        assert "records" in resp
        assert len(resp["records"]) == 2
        assert resp["records"][0]["fields"]["notified"]
        assert resp["records"][1]["fields"]["notified"]
