# Higher-Lower-Game
# 04.04.2022 Rolf Jahnel
# 
from random import randint
from game_data import data
from clear import cls

""" Game-Data
{
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },    
"""

LINE_LEN = 80
max_question = len(data)-1
quest_one = {}
quest_two = {}
question_one = 0
question_two = 0 

def get_questions(switch):   
    global question_one, question_two
    
    if switch:
        question_one = question_two
        temp = question_two
        question_two = randint(0, max_question)
        while question_one == question_two or question_two == temp:
            question_two = randint(0, max_question)
    else:
        while question_one == question_two:
            question_one = randint(0, max_question)
            question_two = randint(0, max_question)
        
    quest_one.update(data[question_one])
    quest_two.update(data[question_two])

def print_logo():
    cls()
    print("== Higher or Lower ==")
    print("-" * LINE_LEN)
    
def print_quest(quest, type):
    
    if type == 'Q':
        print(f"Compare A: {quest['name']}, a {quest['description']}, from {quest['country']}.")
    elif type == 'A':
        print(f"Against B: {quest['name']}, a {quest['description']}, from {quest['country']}.")

def get_greater_follower(questA, questB):
    follower_A = questA["follower_count"]
    follower_B = questB["follower_count"]
    
    if follower_A > follower_B:
        return 'A'
    elif follower_B > follower_A:
        return 'B'
    else:
        return 'X'
    
def ask_answer():
    return input("Who has more followers? Type 'A' or 'B': ").upper()

def print_result(result, score):
    if result == True:
        score += 1
        switch = True
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
    return score
        
playing = True
score = 0
switch = False

while playing:
    print_logo()
    get_questions(switch)
    print_quest(quest_one, 'Q')
    print("        vs")
    print_quest(quest_two, 'A')
    print("." * LINE_LEN)
    answer = ask_answer()
    
    if get_greater_follower(quest_one, quest_two) == answer:
        score = print_result(True, score)
        switch = True
    else:
        score = print_result(False, score)
        playing = False
