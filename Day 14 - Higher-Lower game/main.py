from game_data import data
import random
from art import logo, vs

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def clear_console():
    print("\n" * 50)

def game():
    clear_console()
    print(logo)
    score = 0
    game_should_continue = True

    account_a = get_random_account()
    account_b = get_random_account()

    while account_a == account_b:
        account_b = get_random_account()

    while game_should_continue:
        clear_console()
        print(logo)
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear_console()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            if guess == 'a':
                account_b = get_random_account()
                while account_a == account_b:
                    account_b = get_random_account()
            else:
                account_a = account_b
                account_b = get_random_account()
                while account_a == account_b:
                    account_b = get_random_account()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
            if play_again == 'yes':
                game()
            else:
                game_should_continue = False
                print("Thanks for playing!")

game()