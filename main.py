import turtle
import pandas

screen = turtle.Screen()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

good_guesses_number = 0
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{good_guesses_number}/50 States Correct", prompt="What's another state's name?").title()
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    if answer_state == 'Exit':
        missing_states = [state for state in states_list if state not in guessed_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        x_pos = float(data.x[data.state == answer_state])
        y_pos = float(data.y[data.state == answer_state])
        state.goto(x_pos, y_pos)
        state.write(answer_state, align="center", font=("Arial", 12, "normal"))
        good_guesses_number += 1
        guessed_states.append(answer_state)

