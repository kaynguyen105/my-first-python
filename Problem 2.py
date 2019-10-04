# from Modules.enums import Session
from Modules.enums import Session


class Step:

    def __init__(self, number_of_sessions, number_of_stars):
        self.number_of_sessions = number_of_sessions
        self.number_of_stars = number_of_stars

    def make_step(self):
        sessions_number=int
        star_number=str
        if sessions_number == Session.sessions[int(self.number_of_sessions)] \
                and star_number == Session.star[str(self.number_of_stars)]:
            print("I completed " + Session.sessions[int(self.number_of_sessions)] + " sessions and I rated my expert " +
                  Session.star[str(self.number_of_stars)] + " starts")
        else:
             raise Exception("invalid number of session")


 try:
Step(7, "four").make_step()
 except Exception:
     raise Exception("invalid number of session")


 class InvalidValueException(Exception):
     def __init__(self, message):
         self.message=message







