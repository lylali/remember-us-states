import time
from turtle import Screen,Turtle
import pandas as pd
from screenwrite import Screenwrite

# basic screen and turtle settings
turtle = Turtle()
turtle.penup()
turtle.hideturtle()
screen = Screen()
screen.title("U.S. States Quiz")
screen.bgpic("blank_states_img.gif")
screenwrite = Screenwrite()

# read csv file
data = pd.read_csv("50_states.csv")
state_list = data["state"].to_list()

answer_list = []
# game loop

while len(answer_list) < 50:
    answer = screen.textinput(f"{len(answer_list)} / 50 states correct!.", "Enter your answer.").title()
    if answer == 'Exit':
        break
    if answer in answer_list:
        screenwrite.write_text(f"You already answered {answer}, guess again!")
    else:
        if answer in state_list:
            xcor = int(data[data.state == answer].x)
            ycor = int(data[data.state == answer].y)
            turtle.goto(xcor, ycor)
            turtle.write(f"{answer}", False, 'left', ('Arial', 8, 'bold'))
            answer_list.append(answer)
        else:
            screenwrite.write_text("Your answer is wrong, try again!")

# missed_states_list = [state for state in state_list if not state in answer_list or answer_list.remove(state)]
missed_states_list = [state for state in state_list if state not in answer_list]
# for state in state_list:
#     if state in answer_list:
#         state_list.remove(state)
print(len(missed_states_list))
pd.DataFrame(state_list).to_csv("missing_answers.csv")

