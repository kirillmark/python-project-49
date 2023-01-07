#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.games.gcd import build_qlist, calc_function
from brain_games.games.all_games import games


def main():
    print('Welcome to the Brain Games!')
    player_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    question_list = build_qlist()
    result_list = calc_function(question_list)
    games(player_name, question_list, result_list)


if __name__ == '__main__':
    main()