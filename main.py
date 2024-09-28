import turtle
import pandas

data = pandas.read_csv("./50_states.csv")
screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

all_states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_state) }/50 correct states",
                                     prompt="What's another state's name?").title()
    if answer_states == "Exit":
        missing_states = []
        for states in all_states:
            if states not in guessed_state:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_states in all_states:
        guessed_state.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_states]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_states)