import random
from replit import clear
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Remis!"
    elif computer_score == 0:
        return "Przegrałeś, blackjack!"
    elif user_score == 0:
        return "Wygrałeś, blackjack!"
    elif user_score > 21:
        return "Przekroczyłeś 21, przegrałeś!"
    elif computer_score > 21:
        return "Przeciwnik przekroczył 21, wygrałeś!"
    elif user_score > computer_score:
        return "Wygrałeś!"
    else:
        return "Przegrałeś!"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over: 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Twoje karty: {user_cards}, aktualny wynik: {user_score}")
        print(f"Pierwsza karta przeciwnika: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Czy chcesz dobrać kartę? 't' jeśli tak, 'n' jeśli nie: ")
            if user_should_deal == "t":
                user_cards.append(deal_card())
            elif user_should_deal == "n":
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Twoje karty: {user_cards}, ostateczny wynik: {user_score}")
    print(f"Karty przeciwnika: {computer_cards}, ostateczny wynik: {computer_score}")
    print(compare(user_score, computer_score))
        
while input("Czy chcesz zagrać w Blackjacka? 't' jeśli tak, 'n' jeśli nie: ") == "t":
    clear()
    play_game()
