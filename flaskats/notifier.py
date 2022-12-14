from flaskats.dto import Application

class CandidateNotifier:

    def __init__(self, mail_sender, repository):
        self.sender = mail_sender
        self.repository = repository

    def check_candidates(self):
        #request Rejected/Hired applications
        applications = self.repository.list_records()

        while 'records' in applications: 
            notif = {}
            for app in applications['records']:
                app_dto = Application.from_dict(app['fields'])

                if app_dto.status in ['Hired', 'Rejected'] and app_dto.notified == False:
                    print(f"Candidate {app_dto.name} is {app_dto.status}")
                    if app_dto.status == 'Hired':
                        self.sender.hired_candidate(app_dto)
                        
                    if app_dto.status == 'Rejected':
                        self.sender.rejected_candidate(app_dto)
                                       
                    #add to notified list
                    app_dto.notified = True
                    notif[app['id']] = app_dto.to_dict()

            if len(notif) > 0:
                #update notified field
                self.repository.update_notified_records(notif)
            
            if 'offset' in applications:
                applications = self.repository.list_records(params={'offset': applications['offset']})
            else:
                applications = {}
