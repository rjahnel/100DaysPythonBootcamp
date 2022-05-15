import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
your_cards = []

def line():
    print("-" * 50)
    
def shuffle_cards():
    for _ in range(20):
        random.shuffle(cards)

def give_card():
    return random.choice(cards)

def deal_cards(you, computer):
    if you == 'y':
        your_cards.append(give_card())
    if computer == 'y':
        computer_cards.append(give_card())
    
def print_decks(complete):  
    print(f"Your cards:", end = '')
    for card in your_cards:
        print(f"[{card}] ", end = '')

    print(" ")
    print(f"Computer cards:", end = '')
    if not complete:
        print(f"[{computer_cards[0]}] ", end = '')
    else:
        for card in computer_cards:
            print(f"[{card}] ", end = '')
    print(" ")
    line()
    
def sum_deck(deck):
    deck_sum = 0
    is_eleven = False
    for card in deck:
        if card == 11:
            is_eleven = True
        deck_sum += card
    if deck_sum > 21 and is_eleven:
        deck_sum -= 10    
    return deck_sum
 
def calculate_deck(deck):
    return sum_deck(deck)

def check_deck_ok(deck):
    status = 0    # 0 = OK, 1 = winner, -1 = loose
    sum_of_deck = sum_deck(deck)

    if  sum_of_deck < 21:
        status = 0
    elif sum_of_deck == 21:
        status = 1
    elif sum_of_deck > 21:
        status = -1
    return status

def check_results():
    you = calculate_deck(your_cards)
    computer = calculate_deck(computer_cards)
    you_cardcount = len(your_cards)
    computer_cardcount = len(computer_cards)
    
    if you == computer:
        print(f"It is a tie - your score [{you}] - computer [{computer}]")
    elif you > 21 and computer <= 21:
        print(f"You loose! - your score [{you}] - computer [{computer}]")
    elif computer > 21 and you <= 21:
        print(f"You win! - your score [{you}] - computer [{computer}]")
    elif you > 21 and computer > 21:
        print(f"Both loose! - your score [{you}] - computer [{computer}]")
    elif computer > 21 and you > 21:
        print(f"Both loose! - your score [{you}] - computer [{computer}]")
    elif you == 21 and you_cardcount == 2:
        print("You have a BLACKJACK!!!")
    elif computer == 21 and computer_cardcount == 2:
        print("The computer has a BLACKJACK!!!")    
    elif you == 21 or you > computer and you <= 21:
        print(f"You win! - your score [{you}] - computer [{computer}]")
    elif computer == 21 or you < computer and computer <= 21:
        print(f"You loose! - your score [{you}] - computer [{computer}]")
    
# Dealer must stand on 17 and must draw to 16        
def deal_computer(): 
    while sum_deck(computer_cards) < 17:
        deal_cards('n', 'y')        
   
# ========== Start game =============
shuffle_cards()
for _ in range(2):
    deal_cards('y', 'y')
print_decks(False)

playing = True

while playing:  
    you = check_deck_ok(your_cards)
    computer = check_deck_ok(computer_cards)

    if  you != 0:
        playing = False
    elif computer != 0:
        playing = False
    else:
        next_you = input("One more card ('y' = yes, 'n' = no)? ")
        deal_computer()

        if next_you != 'n':
            deal_cards(next_you, 'n')
            print_decks(False)        
        else:
            playing = False
            
line()            
check_results()
print_decks(True)
print("Game over!")
