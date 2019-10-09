from Modules.enums import Session


class Step:

    def __init__(self, number_of_sessions, number_of_stars):
        self.number_of_sessions = number_of_sessions
        self.number_of_stars = number_of_stars

    def make_step(self):
        message1 = "Invalid number of sessions"
        message2 = "Invalid number of stars"
        if self.number_of_sessions not in Session.NUMBER_TO_TEXT_MAP["SESSIONS"].keys():
            raise InvalidValueException(message1)
        if self.number_of_stars not in Session.NUMBER_TO_TEXT_MAP["STARS"].keys():
            raise InvalidValueException(message2)
        print("I completed "
                                       + Session.NUMBER_TO_TEXT_MAP["SESSIONS"][self.number_of_sessions]
                                       + " sessions and I rated my expert "
                                       + str(Session.NUMBER_TO_TEXT_MAP["STARS"][self.number_of_stars])
                                       + " starts")


class InvalidValueException(Exception):
    def __init__(self, message):
        self.message = message
try:
    Step(9, "fdour").make_step()
except InvalidValueException as e:
    print(e)

