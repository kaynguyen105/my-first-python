# from Modules.enums import Session
from Modules.enums import Session


class Step():

    def __init__(self, number_of_sessions, number_of_stars):
        self.number_of_sessions = number_of_sessions
        self.number_of_stars = number_of_stars

    def make_step(self):

        sessions_number = Session.sessions[int(self.number_of_sessions)]

        star_number = Session.star[str(self.number_of_stars)]
        print("I completed " + sessions_number + " sessions and I rated my expert " + str(star_number) + " starts")
# Step(9, "four").make_step()

class InvalidValueException(Exception):
    def __init__(self, message):
        self.message=message
try:
    a=Step.number_of_sessions
    int(a)
    b=Step.number_of_stars
    str(b)
    a>0 and a<10
except:
    raise InvalidValueException("Invalid number of sessions")






#      def invalid_value_exception(self):
#          try:
#              sessions_number = Session.sessions[int(self.number_of_sessions)]
#              star_number = Session.star[str(self.number_of_stars)]
#
#          except:
#              print("Invalid number of sessions")


