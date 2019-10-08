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
            if self.number_of_sessions not in Session.NUMBER_TO_TEXT_MAP["SESSIONS"].keys():
                print("Invalid number of sessions")
            elif self.number_of_stars not in Session.NUMBER_TO_TEXT_MAP["STARS"].keys():
                print("Invalid number of starts")


Step(9, "four").make_step()


a = Step(9, "five")
a.make_step()
