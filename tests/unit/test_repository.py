from pytest import mock
from flaskats.repository import AirtableRepository

class TestRepository:
      
    LIST_RESPONSE = '''
    {
      "records": [
        {
          "createdTime": "2022-09-12T21:03:48.000Z",
          "fields": {
            "name": "AName AndSurname"
            "email": "mail@gmail.com"
            "job": "ABC-123"
            "date": "2022-09-12T21:03:48.000Z"
            "status": "Inbox"
            "notified": false
          },
          "id": "rec560UJdUtocSouk"
        },
        {
          "createdTime": "2022-09-12T21:03:48.000Z",
          "fields": {
            "name": "AName2 AndSurname2"
            "email": "mail2@gmail.com"
            "job": "ABC-123"
            "date": "2022-09-12T21:03:48.000Z"
            "status": "Inbox"
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
            "name": "AName AndSurname"
            "email": "mail@gmail.com"
            "notified": false
            },
            "id": "rec560UJdUtocSouk"
          },
          {
          "fields": {
            "name": "AName2 AndSurname2"
            "email": "mail2@gmail.com"
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
            "name": "AName AndSurname"
            "email": "mail@gmail.com"
            "notified": true
            },
            "id": "rec560UJdUtocSouk"
          },
          {
          "fields": {
            "name": "AName2 AndSurname2"
            "email": "mail2@gmail.com"
            "notified": true
            },
            "id": "rec3lbPRG4aVqkeOQ"
          }
        ]
      }'
    '''

    @requests_mock.Mocker()
    def test_create_record(self):
        with requests_mock.Mocker() as m:
            m.get(AirtableRepository.records_url, text=self.LIST_RESPONSE)

            repo = AirtableRepository()
            resp = repo.list_records()
        assert resp.text == self.LIST_RESPONSE

    #@requests_mock.Mocker()
    def test_list_records(self):
        with requests_mock.Mocker() as m:
            m.get(AirtableRepository.records_url, text=self.LIST_RESPONSE)

            repo = AirtableRepository()
            resp = repo.list_records()
        assert resp.text == self.LIST_RESPONSE

    @requests_mock.Mocker()
    def test__create_json_update(self,application_dtos):
        repo = AirtableRepository()
        result = repo._create_json_update(application_dtos)
        assert "records" in result
        assert len(result["records"]) == 2
        assert application_dtos[1].name in result["records"][1]["fields"]["name"]

    @requests_mock.Mocker()
    def test_update_notified_records(self,application_dtos):
        with requests_mock.Mocker() as m:
            m.patch(AirtableRepository.records_url, text=self.UPDATE_RESPONSE)

            repo = AirtableRepository()
            resp = repo.update_notified_records(application_dtos)
            assert "records" in resp
            assert len(resp["records"]) == 2
            assert resp["records"][0]["fields"]["notified"]
            assert resp["records"][1]["fields"]["notified"]
