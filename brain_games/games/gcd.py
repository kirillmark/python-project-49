import random
from math import gcd


def build_qlist():
    qlist = []
    for i in range(3):
        first_number = random.randint(2, 70)
        second_number = random.randint(2, 70)
        res_sing = f'{first_number} {second_number}'
        qlist.append(res_sing)
    return qlist


def calc_function(list_for_eval):
    rlist = []
    for elem in list_for_eval:
        first_number, second_number = map(int, elem.split())
        result = gcd(first_number, second_number)
        rlist.append(result)
    return rlist
