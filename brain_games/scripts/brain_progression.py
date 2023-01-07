#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.games.progression import build_qlist
from brain_games.games.all_games import games


def main():
    print('Welcome to the Brain Games!')
    player_name = welcome_user()
    print('What number is missing in the progression?')
    question_list, result_list = build_qlist()
    games(player_name, question_list, result_list)


if __name__ == '__main__':
    main()
