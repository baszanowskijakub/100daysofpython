import random

print('''
  .------. .------. 
 |A_  _ | |A .   | 
 |( \/ )| | / \  | 
 | \  / | |(_,_) | 
 |  \/ A||  I  A | 
 `------' `------'
''')


def get_card_value(card, current_score):
    rank = card.split(" ")[0]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 1 if current_score + 11 > 21 else 11
    else:
        return int(rank)


def draw(hand, score):
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)
    return get_card_value(card, score)


while True:
    game_continue = True
    player_score = 0
    computer_score = 0
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]
    random.shuffle(deck)
    player_hand = []
    computer_hand = []

    game_start = input("Do you want to play Blackjack? Type 'y' or 'n': ")
    if game_start != "y":
        print("Bye, bye then!")
        break

    player_score += draw(player_hand, player_score)
    computer_score += draw(computer_hand, computer_score)
    print(f"Your hand is: {player_hand}, Score: {player_score}")
    print(f"Computer's hand is {computer_hand}, Score: {computer_score}")

    while game_continue:
        decision = input("Do you want to hit? Type 'y' or 'n': ")
        if decision == "y":
            player_score += draw(player_hand, player_score)
            print(f"Your hand is: {player_hand}, Score: {player_score}")
            if player_score > 21:
                print("You lose")
                game_continue = False
        else:
            while computer_score < 17 and computer_score < player_score:
                computer_score += draw(computer_hand, computer_score)
            print(f"Computer's hand is {computer_hand}, Score: {computer_score}")
            if computer_score > 21:
                print("Computer busts, you win!")
                game_continue = False
            elif computer_score >= player_score:
                print("Computer wins!")
                game_continue = False

    replay = input("Do you want to play again? Type 'y' or 'n': ")
    if replay != "y":
        print("Thanks for playing! Goodbye.")
        break