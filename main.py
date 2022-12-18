import random
import art
import os
from game_data import data

# compare() calculates which choice has more followers and checks if user's answer is that choice. Returns bool
def compare(choice_a: dict, choice_b: dict) -> bool:
    user_answer = input('Who has more instagram followers? Type "A" or "B": ').lower()
    
    if choice_a['follower_count'] > choice_b['follower_count']:
        solution = 'a'
    elif choice_b['follower_count'] > choice_a['follower_count']:
        solution = 'b'
    else:
        solution = user_answer
        
    if user_answer == solution:
        return True
    else: 
        return False

# coninue_game() calls compare(). While compare returns True game will continue. Returns final score
def continue_game(subject1: dict, subject2: dict) -> int:
    end = compare(choice_a = subject1, choice_b = subject2)
    score = 0
    
    while end:
        os.system('cls')
        score += 1
        print(f"You're right! Current score: {score}.")
        subject1 = subject2
        subject2 = random.choice(data)
        print_UI(subject1 = subject1, subject2 = subject2)
        end = compare(choice_a = subject1, choice_b = subject2)
    return score

# print_UI() prints artwork and two random data to console
def print_UI(subject1: dict, subject2: dict):
    print(art.logo)
    print(f"Compare A: {subject1['name']}, a {subject1['description']}, from {subject1['country']}.")
    print(art.vs)
    print(f"Compare B: {subject2['name']}, a {subject2['description']}, from {subject2['country']}.")
    
def play():
    subject1 = random.choice(data)
    subject2 = random.choice(data)
    
    print_UI(subject1 = subject1, subject2 = subject2)
    final_score = continue_game(subject1 = subject1, subject2 = subject2)
    os.system('cls')
    print(art.logo)
    print(f"Sorry, that's the wrong answer. Final score: {final_score}.")

if __name__ == '__main__':
    play()
