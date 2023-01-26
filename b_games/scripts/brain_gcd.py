#!/usr/bin/env python3
from b_games.games.gcd import build_qlist, build_alist
from b_games.games.all_games import games


def main():
    rules = 'Find the greatest common divisor of given numbers.'
    games(rules, build_qlist, build_alist)


if __name__ == '__main__':
    main()
