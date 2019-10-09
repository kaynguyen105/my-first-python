from Modules.enums import Session


class Step:

    def __init__(self, number_of_sessions, number_of_stars):
        self.number_of_sessions = number_of_sessions
        self.number_of_stars = number_of_stars

    def make_step(self):
        message1 = "Invalid number of sessions"
        message2 = "Invalid number of stars"
        try:
            if self.number_of_sessions in Session.NUMBER_TO_TEXT_MAP["SESSIONS"].keys():
                if self.number_of_stars in Session.NUMBER_TO_TEXT_MAP["STARS"].keys():
                    print("I completed "
                                       + Session.NUMBER_TO_TEXT_MAP["SESSIONS"][self.number_of_sessions]
                                       + " sessions and I rated my expert "
                                       + str(Session.NUMBER_TO_TEXT_MAP["STARS"][self.number_of_stars])
                                       + " starts")
                else:
                    raise InvalidValueException(message2)
            else:
                raise InvalidValueException(message1)
        except InvalidValueException as e:
            print(e)


class InvalidValueException(Exception):
    def __init__(self, message):
        self.message = message


Step(9, "four").make_step()
