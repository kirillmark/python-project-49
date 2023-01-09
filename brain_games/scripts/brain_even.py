#!/usr/bin/env python3
from brain_games.games.even import build_qlist, calc_function
from brain_games.games.all_games import games


def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    question_list = build_qlist()
    result_list = calc_function(question_list)
    games(rules, question_list, result_list)


if __name__ == '__main__':
    main()
