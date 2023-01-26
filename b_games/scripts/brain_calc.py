#!/usr/bin/env python3
from b_games.games.all_games import games
from b_games.games.calc import build_qlist, build_alist


def main():
    rules = 'What is the result of the expression?'
    games(rules, build_qlist, build_alist)


if __name__ == '__main__':
    main()
