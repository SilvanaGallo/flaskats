class Candidate:
    def __init__(**kargs):
        self.name = kargs['name']
        self.email= kargs['email']

class Application:
    def __init__(**kargs):
        self.job = kargs['code']
        self.date= kargs['date']
        