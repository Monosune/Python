import pandas
import turtle


class StateGame:
    def __init__(self):
        self.states_data = pandas.read_csv("50_states.csv")
        self.state = self.states_data["state"].tolist()
        self.score = 0

    def naming_states(self, answer):
        state_info = self.states_data[self.states_data["state"] == answer]
        if answer in self.state:
            turtle.penup()
            turtle.hideturtle()
            turtle.goto(int(state_info.x), int(state_info.y))
            turtle.write(answer)
            self.score_up()

    def score_up(self):
        self.score += 1




