#!/usr/bin/env python3
from brain_games.games.progression import build_qlist
from brain_games.games.all_games import games


def main():
    rules = 'What number is missing in the progression?'
    question_list, result_list = build_qlist()
    games(rules, question_list, result_list)


if __name__ == '__main__':
    main()
