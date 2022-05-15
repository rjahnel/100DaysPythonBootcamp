# https://www.sporcle.com/games/g/states
import turtle
import pandas

score = 0
correct_guesses = []
game_is_on = True
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
max_states = len(all_states)

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("U.S. States Game")
screen.addshape(image)
turtle.setup(width=750, height=510, startx=None, starty=None)
turtle.shape(image)
write = turtle.Turtle()
write.hideturtle()
write.penup()

while game_is_on:
    title = f"{score}/{max_states} States correct"
    answer_state = screen.textinput(title=title, prompt="What's another state name?").title()

    if score == max_states:
        game_is_on = False
    elif answer_state == "Exit":
        game_is_on = False
        missing_states = [state for state in all_states if state not in correct_guesses]
        learn_data = pandas.DataFrame(missing_states)
        learn_data.to_csv("states_to_learn.csv")
        for state in all_states:
            if state not in correct_guesses:
                state_data = data[data.state == state]
                write.color('green')
                write.setposition(int(state_data.x), int(state_data.y))
                write.write(state_data.state.item())
    elif answer_state in all_states and answer_state not in correct_guesses:
        state_data = data[data.state == answer_state]
        write.setposition(int(state_data.x), int(state_data.y))
        write.write(answer_state)
        correct_guesses.append(answer_state)
        score += 1

screen.exitonclick()