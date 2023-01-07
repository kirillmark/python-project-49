import random


def build_qlist():
    qlist = []
    for i in range(3):
        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)
        sign = random.choice(['+', '-', '*'])
        res_sing = f'{first_number} {sign} {second_number}'
        qlist.append(res_sing)
    return qlist


def calc_function(list_for_eval):
    rlist = []
    for elem in list_for_eval:
        result = eval(elem)
        rlist.append(result)
    return rlist
