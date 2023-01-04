#!/usr/bin/env python3
from brain_games.cli import welcome_user
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    player_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer = 0
    while correct_answer != 3:
        random_int = random.randint(1, 100)
        print(f'Question: {random_int}')
        user_answer = prompt.string('Your answer: ')
        if random_int % 2 == 0 and user_answer == 'yes' or random_int % 2 != 0 and user_answer == 'no':
            print('Correct!')
            correct_answer += 1
        else:
            if user_answer == 'yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again {player_name}")
                break
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again {player_name}")
                break
    else:
        print(f'Congratulations, {player_name}!')


if __name__ == '__main__':
    main()
