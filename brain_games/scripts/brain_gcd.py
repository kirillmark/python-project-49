#!/usr/bin/env python3
from brain_games.cli import welcome_user
import random
import prompt
from math import gcd


def main():
    print('Welcome to the Brain Games!')
    player_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    answer = 0
    while answer != 3:
        first_number = random.randint(2, 70)
        second_number = random.randint(2, 70)
        print(f'Question: {first_number} {second_number}')
        user_answer = prompt.string('Your answer: ')
        right_res = gcd(first_number, second_number)
        if int(user_answer) == right_res:
            print('Correct!')
            answer += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_res}'.")
            print(f"Let's try again, {player_name}!")
            break
    else:
        print(f'Congratulations, {player_name}')


if __name__ == '__main__':
    main()