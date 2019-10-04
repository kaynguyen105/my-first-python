from Modules.enums import Session


class Step:

    def __init__(self, number_of_sessions, number_of_stars):
        self.number_of_sessions = number_of_sessions
        self.number_of_stars = number_of_stars

    def make_step(self):
        if (self.number_of_sessions in Session.NUMBER_TO_TEXT_MAP["SESSIONS"].keys()) and \
                (self.number_of_stars in Session.NUMBER_TO_TEXT_MAP["STARS"].keys()):
            print("I completed "
                  + Session.NUMBER_TO_TEXT_MAP["SESSIONS"][self.number_of_sessions]
                  + " sessions and I rated my expert "
                  + str(Session.NUMBER_TO_TEXT_MAP["STARS"][self.number_of_stars])
                  + " starts")
        else:
            if self.number_of_sessions not in Session.NUMBER_TO_TEXT_MAP["SESSIONS"].keys():
                print("Invalid number of sessions")
            else:
                if self.number_of_stars not in Session.NUMBER_TO_TEXT_MAP["STARS"].keys():
                    print("Invalid number of starts")

Step(22, "two").make_step()

class InvalidValueException(Exception):
    def __init__(self, message1, message2):
        self.message1 = message1
        self.message2 = message2


# if __name__ == '__main__':
#     Step(2, "four").make_step()
#     message1 = "Invalid number of stars"
#     message2 = "Invalid number of sessions"
#     if (Step.make_step.(self.number_of_sessions)) in Session.NUMBER_TO_TEXT_MAP["SESSIONS"].keys()) and \
#                 (Step.number_of_sessions in Session.NUMBER_TO_TEXT_MAP["STARS"].keys()):
#         raise InvalidValueException(message1)








