#!/usr/bin/env python3
from b_games.games.progression import build_qlist, build_alist
from b_games.games.all_games import games


def main():
    rules = 'What number is missing in the progression?'
    games(rules, build_qlist, build_alist)


if __name__ == '__main__':
    main()
