import pandas
import turtle
from game import StateGame

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic("blank_states_img.gif")
game = StateGame()

playing = True

while playing:
    score = game.score
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?").capitalize()
    game.naming_states(answer_state)


screen.exitonclick()

