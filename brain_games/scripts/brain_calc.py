#!/usr/bin/env python3
from brain_games.cli import welcome_user
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    player_name = welcome_user()
    print('What is the result of the expression?')
    right_answer = 0
    while right_answer != 3:
        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)
        sign = random.choice(['+', '-', '*'])
        res_sing = f'{first_number} {sign} {second_number}'
        print(f'Question: {res_sing}')
        user_answer = prompt.string('Your answer: ')
        result = eval(res_sing)
        if int(user_answer) == result:
            print('Correct!')
            right_answer += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {player_name}!")
            break
    else:
        print(f'Congratulations, {player_name}!')


if __name__ == '__main__':
    main()