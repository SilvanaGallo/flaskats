from flaskats.dtos import Application
from flaskats.models import ApplicationStatus
from flaskats.services import Producer


class CandidateNotifier:

    def __init__(self, mail_sender, repository):
        self.sender = mail_sender
        self.repository = repository

    def check_candidates(self):

        # request Rejected/Hired applications
        applications = self.repository.list_records()
        while 'records' in applications:
            notif: dict = {}
            for app in applications['records']:
                app_dto: Application = Application.from_dict(app)

                if app_dto.status in [ApplicationStatus.HIRED, ApplicationStatus.REJECTED] and app_dto.notified is False:
                    print(f"Candidate {app_dto.name} is {app_dto.status}")
                    if app_dto.status is ApplicationStatus.HIRED:
                        # Queue application
                        producer = Producer(queue='hired')
                        producer.submit_event(app_dto)

                    if app_dto.status is ApplicationStatus.REJECTED:
                        self.sender.rejected_candidate(app_dto)

                    # add to notified dict
                    app_dto.notified = True
                    notif[app_dto.candidate_id] = app_dto.to_dict()

            if len(notif) > 0:
                # update notified field
                self.repository.update_notified_records(notif)

            if 'offset' in applications:
                applications = self.repository.list_records(
                                    params={'offset': applications['offset']})
            else:
                applications = {}
