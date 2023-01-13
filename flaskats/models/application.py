from enum import Enum


class ApplicationStatus(Enum):
    INBOX = 1
    HIRED = 2
    REJECTED = 3

    def __str__(self):
        return str(self.name)