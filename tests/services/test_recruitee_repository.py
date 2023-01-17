import pytest
from unittest import mock
from unittest.mock import Mock
from flaskats.dtos import Application
from flaskats.services import RecruiteeRepository
from flaskats.repositories import SQLAlchemyOffersRepository


class TestRecruiteeRepository:

    CREATE_RESPONSE = '''{
                            "candidate": {
                                "in_active_share": false,
                                "ratings": {},
                                "gdpr_status": "no_consent",
                                "has_avatar": false,
                                "source": "manual",
                                "viewed": false,
                                "notes_count": 0,
                                "pending_result_request": false,
                                "tasks_count": 0,
                                "links": [],
                                "social_links": [],
                                "attachments_count": 0,
                                "sourcing_data": null,
                                "grouped_open_question_answers": [],
                                "id": 46573203,
                                "followed": false,
                                "custom_fields": [],
                                "gdpr_consent_request_completed_at": null,
                                "cv_url": null,
                                "unread_notifications": false,
                                "phones": [],
                                "name": "AName AndSurname",
                                "referral_referrers_ids": [],
                                "admin_ids": [],
                                "placements": [],
                                "my_last_rating": null,
                                "my_pending_result_request": false,
                                "initials": "A",
                                "upcoming_event": false,
                                "fields": [
                                {
                                    "fixed": true,
                                    "id": null,
                                    "kind": "education",
                                    "origin": "manual",
                                    "values": [],
                                    "visibility": {
                                    "admin_ids": [],
                                    "level": "public",
                                    "role_ids": []
                                    },
                                    "visible": true
                                },
                                {
                                    "fixed": true,
                                    "id": null,
                                    "kind": "experience",
                                    "origin": "manual",
                                    "values": [],
                                    "visibility": {
                                    "admin_ids": [],
                                    "level": "public",
                                    "role_ids": []
                                    },
                                    "visible": true
                                }
                                ],
                                "open_question_answers": [],
                                "referrer": null,
                                "gdpr_expires_at": null,
                                "gdpr_scheduled_to_delete_at": null,
                                "admin_id": 316045,
                                "my_upcoming_event": false,
                                "updated_at": "2023-01-15T16:56:58.161904Z",
                                "photo_url": "https://recruitee-main.s3.eu-central-1.amazonaws.com/candidates/46573203/normal_photo_g35r7b86mea8.png",
                                "sources": [],
                                "cv_processing_status": "ok",
                                "adminapp_url": "https://app.recruitee.com/#/dashboard/overview?candidate=46573203&company=89564",
                                "cv_original_url": null,
                                "ratings_count": 0,
                                "gdpr_consent_request_type": null,
                                "created_at": "2023-01-15T16:56:58.161904Z",
                                "rating_visible": true,
                                "gdpr_consent_request_sent_at": null,
                                "pending_request_link": false,
                                "emails": ["mail@gmail.com"],
                                "tags": [],
                                "sourcing_origin": null,
                                "gdpr_consent_ever_given": false,
                                "example": false,
                                "mailbox_messages_count": 0,
                                "cover_letter": null,
                                "last_activity_at": "2023-01-15T16:56:58.161904Z",
                                "positive_ratings": null,
                                "duplicates": [],
                                "online_data": null,
                                "photo_thumb_url": "https://recruitee-main.s3.eu-central-1.amazonaws.com/candidates/46573203/thumb_photo_g35r7b86mea8.png",
                                "rating": 0,
                                "last_message_at": null
                            },
                            "references": [
                                {
                                "email": "silvana.lis@jobandtalent.com",
                                "first_name": "Silvana",
                                "has_avatar": false,
                                "id": 316045,
                                "initials": "SG",
                                "last_name": "Gallo",
                                "photo_normal_url": "https://recruitee-main.s3.eu-central-1.amazonaws.com/admins/316045/normal_avatar_sh6np58o2e3w.png",
                                "photo_thumb_url": "https://recruitee-main.s3.eu-central-1.amazonaws.com/admins/316045/thumb_avatar_sh6np58o2e3w.png",
                                "time_format24": true,
                                "timezone": "America/New_York",
                                "type": "Admin"
                                }
                            ]
                            }
    '''

    LIST_RESPONSE = '''{
                        "candidates": [
                            {
                                "admin_id": null,
                                "adminapp_url": "https://app.recruitee.com/#/dashboard/overview?candidate=46044144&company=89564",
                                "created_at": "2022-12-19T13:28:15.341931Z",
                                "emails": [
                                    "wilmaroelendsen@recruiteemail.com"
                                ],
                                "example": true,
                                "followed": false,
                                "has_avatar": true,
                                "id": 46044144,
                                "initials": "WR",
                                "last_message_at": null,
                                "my_last_rating": null,
                                "my_pending_result_request": false,
                                "my_upcoming_event": false,
                                "name": "Wilma Roelendsen (Sample)",
                                "notes_count": 1,
                                "pending_result_request": false,
                                "phones": [
                                    "+15555555555"
                                ],
                                "photo_thumb_url": "https://recruitee-main.s3.eu-central-1.amazonaws.com/candidates/46044144/thumb_photo_lpvwubg9lsua.jpg",
                                "placements": [
                                    {
                                        "candidate_id": 46044144,
                                        "created_at": "2022-12-19T13:28:15.341931Z",
                                        "hired_at": "2023-01-04T11:22:49.178555Z",
                                        "hired_by_id": 316045,
                                        "hired_in_other_placement": false,
                                        "hired_in_this_placement": false,
                                        "id": 48791516,
                                        "job_starts_at": null,
                                        "language": null,
                                        "offer_id": 1181300,
                                        "overdue_at": null,
                                        "overdue_diff": null,
                                        "position": 1,
                                        "positive_ratings": null,
                                        "ratings": {},
                                        "stage_id": 8063179,
                                        "updated_at": "2023-01-04T11:22:49.181484Z"
                                    }
                                ],
                                "positive_ratings": 75,
                                "rating": 0,
                                "ratings": {
                                    "yes": 1
                                },
                                "ratings_count": 1,
                                "referrer": "Indeed",
                                "source": "career_site",
                                "tasks_count": 1,
                                "unread_notifications": false,
                                "upcoming_event": false,
                                "updated_at": "2022-12-19T13:28:15.341931Z",
                                "viewed": true
                            },
                            {
                                "admin_id": null,
                                "adminapp_url": "https://app.recruitee.com/#/dashboard/overview?candidate=46044126&company=89564",
                                "created_at": "2022-12-18T13:28:05.451549Z",
                                "emails": [
                                    "johndoe@recruiteemail.com"
                                ],
                                "example": true,
                                "followed": false,
                                "has_avatar": true,
                                "id": 46044126,
                                "initials": "JD",
                                "last_message_at": null,
                                "my_last_rating": null,
                                "my_pending_result_request": false,
                                "my_upcoming_event": false,
                                "name": "John Doe (Sample)",
                                "notes_count": 1,
                                "pending_result_request": false,
                                "phones": [
                                    "+15555555555"
                                ],
                                "photo_thumb_url": "https://recruitee-main.s3.eu-central-1.amazonaws.com/candidates/46044126/thumb_photo_kapb94pwewvh.jpg",
                                "placements": [
                                    {
                                        "candidate_id": 46044126,
                                        "created_at": "2022-12-18T13:28:05.451549Z",
                                        "disqualify_kind": "admin",
                                        "disqualify_reason": "Wrong skill set",
                                        "hired_at": null,
                                        "hired_by_id": null,
                                        "hired_in_other_placement": false,
                                        "hired_in_this_placement": false,
                                        "id": 48791494,
                                        "job_starts_at": null,
                                        "language": null,
                                        "offer_id": 1181299,
                                        "overdue_at": null,
                                        "overdue_diff": null,
                                        "position": 1,
                                        "positive_ratings": null,
                                        "ratings": {},
                                        "stage_id": 8063167,
                                        "updated_at": "2023-01-04T11:47:16.388666Z"
                                    }
                                ],
                                "positive_ratings": null,
                                "rating": 0,
                                "ratings": {},
                                "ratings_count": 0,
                                "referrer": "Indeed",
                                "source": "career_site",
                                "tasks_count": 0,
                                "unread_notifications": false,
                                "upcoming_event": false,
                                "updated_at": "2022-12-18T13:28:05.451549Z",
                                "viewed": true
                            },
                            {
                                "admin_id": 152125,
                                "adminapp_url": "https://app.recruitee.com/#/dashboard/overview?candidate=46044140&company=89564",
                                "created_at": "2022-12-16T13:28:15.340859Z",
                                "emails": [
                                    "conormoreno@recruiteemail.com"
                                ],
                                "example": true,
                                "followed": false,
                                "has_avatar": true,
                                "id": 46044140,
                                "initials": "CM",
                                "last_message_at": null,
                                "my_last_rating": null,
                                "my_pending_result_request": false,
                                "my_upcoming_event": false,
                                "name": "Conor Moreno (Sample)",
                                "notes_count": 1,
                                "pending_result_request": false,
                                "phones": [
                                    "+15555555555"
                                ],
                                "photo_thumb_url": "https://recruitee-main.s3.eu-central-1.amazonaws.com/candidates/46044140/thumb_photo_mnlkmwo68lk3.jpg",
                                "placements": [
                                    {
                                        "candidate_id": 46044140,
                                        "created_at": "2022-12-16T13:28:15.340859Z",
                                        "hired_at": null,
                                        "hired_by_id": null,
                                        "hired_in_other_placement": false,
                                        "hired_in_this_placement": false,
                                        "id": 48791511,
                                        "job_starts_at": null,
                                        "language": null,
                                        "offer_id": 1181300,
                                        "overdue_at": null,
                                        "overdue_diff": null,
                                        "position": 1,
                                        "positive_ratings": null,
                                        "ratings": {},
                                        "stage_id": 8063175,
                                        "updated_at": "2022-12-16T13:28:15.340859Z"
                                    }
                                ],
                                "positive_ratings": 0,
                                "rating": 0,
                                "ratings": {
                                    "no": 1
                                },
                                "ratings_count": 1,
                                "referrer": "Facebook",
                                "source": "import",
                                "tasks_count": 1,
                                "unread_notifications": false,
                                "upcoming_event": false,
                                "updated_at": "2022-12-16T13:28:15.340859Z",
                                "viewed": true
                            }
                        ],
                        "generated_at": "2023-01-04T11:56:15.366778Z",
                        "references": [
                            {
                                "department_id": 288442,
                                "guid": "ptgrp",
                                "id": 1181300,
                                "kind": "job",
                                "lang_code": "en",
                                "location": "Remote job",
                                "position": 2,
                                "slug": "recruiter-sample",
                                "status": "internal",
                                "title": "Recruiter (Sample)",
                                "type": "Offer"
                            },
                            {
                                "category": "hire",
                                "created_at": "2023-01-03T13:28:05.434325Z",
                                "fair_evaluations_enabled": false,
                                "group": null,
                                "id": 8063179,
                                "locked": false,
                                "name": "Hired",
                                "placements_count": null,
                                "position": 5,
                                "time_limit": null,
                                "type": "Stage",
                                "updated_at": "2023-01-03T13:28:05.434327Z"
                            },
                            {
                                "department_id": 288443,
                                "guid": "pmgs8",
                                "id": 1181299,
                                "kind": "job",
                                "lang_code": "en",
                                "location": "New York, United States",
                                "position": 4,
                                "slug": "senior-marketer-sample-london",
                                "status": "published",
                                "title": "Senior Marketer (Sample)",
                                "type": "Offer"
                            },
                            {
                                "category": "apply",
                                "created_at": "2023-01-03T13:28:05.434300Z",
                                "fair_evaluations_enabled": false,
                                "group": null,
                                "id": 8063167,
                                "locked": true,
                                "name": "Applied",
                                "placements_count": null,
                                "position": -1,
                                "time_limit": null,
                                "type": "Stage",
                                "updated_at": "2023-01-03T13:28:05.434301Z"
                            },
                            {
                                "category": "apply",
                                "created_at": "2023-01-03T13:28:05.434300Z",
                                "fair_evaluations_enabled": false,
                                "group": null,
                                "id": 8063175,
                                "locked": true,
                                "name": "Applied",
                                "placements_count": null,
                                "position": -1,
                                "time_limit": null,
                                "type": "Stage",
                                "updated_at": "2023-01-03T13:28:05.434301Z"
                            },
                            {
                                "email": "john.assistant@recruitee.com",
                                "first_name": "John",
                                "has_avatar": false,
                                "id": 152125,
                                "initials": "JT",
                                "last_name": "The assistant",
                                "photo_normal_url": "https://recruitee-main.s3.eu-central-1.amazonaws.com/admins/152125/normal_avatar_e592g7dlybt3.jpg",
                                "photo_thumb_url": "https://recruitee-main.s3.eu-central-1.amazonaws.com/admins/152125/thumb_avatar_e592g7dlybt3.jpg",
                                "time_format24": true,
                                "timezone": "Europe/Warsaw",
                                "type": "Admin"
                            }
                        ]
                    }'''

    UPDATE_RESPONSE = '''{ "uuid": "11ae-34343-4343-434" }'''

    @pytest.mark.unit
    def test_create_record(self, requests_mock, application_dtos):
        requests_mock.post(RecruiteeRepository.candidates_url, text=self.CREATE_RESPONSE)

        repo = RecruiteeRepository()
        application = Application.from_dict(application_dtos["rec560UJdUtocSouk"])
        resp = repo.create_record(application)

        assert "id" in resp["candidate"]
        assert resp["candidate"]["name"] == application_dtos["rec560UJdUtocSouk"]["name"]
        assert resp["candidate"]["emails"][0] == application_dtos["rec560UJdUtocSouk"]["email"]

    @pytest.mark.unit
    # @mock.patch('flaskats.services.RecruiteeRepository.SQLAlchemyOffersRepository', spec=SQLAlchemyOffersRepository)
    def test_list_records(self, requests_mock):
        assert False
        # requests_mock.get(RecruiteeRepository.candidates_url, text=self.LIST_RESPONSE)
        # offers_repository = Mock()
        # offers_repository.return_value.get_offer_by_repository_id.return_value.code.return_value = "ABC-123"

        # repo = RecruiteeRepository()
        # resp = repo.list_records()

        # assert len(resp["records"]) == 3
        # assert resp["records"][0]["name"] == "Wilma Roelendsen (Sample)"

    @pytest.mark.unit
    def test__create_json_update(self, application_dtos):
        repo = RecruiteeRepository()

        result = repo._create_json_update(application_dtos)
        assert "candidates" in result
        assert len(result["candidates"]) == 2
        assert result["candidates"][0] == "rec560UJdUtocSouk"
        assert result["tags"] == ["notified"]

    @pytest.mark.unit
    @mock.patch("flaskats.services.RecruiteeRepository.requests.patch")
    def test_update_notified_records(self, mock_requests_patch, application_dtos):
        #assert False
        mock_requests_patch.return_value = mock.Mock(**{"status_code": 200,
                                "json.return_value": self.UPDATE_RESPONSE})
        repo = RecruiteeRepository()
        resp = repo.update_notified_records(application_dtos)

        assert len(resp["status_code"]) == 200
        assert "uuid" in resp

    @pytest.mark.unit
    def test_get_candidate(self):
        assert False
    #     url = f"{self.candidates_url}/{app_dto.candidate_id}"
    #     response = requests.get(url, headers=self.headers)
    #     return response

    @pytest.mark.unit
    def test_get_notified(self):
        assert False
    #  -> bool:
    #     response = self.get_candidate(app_dto)
    #     response = response.json()
    #     return "notified" in response["candidate"]["tags"]