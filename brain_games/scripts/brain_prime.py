#!/usr/bin/env python3
from brain_games.games.prime import build_qlist, build_alist
from brain_games.games.all_games import games


def main():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    games(rules, build_qlist, build_alist)


if __name__ == '__main__':
    main()
