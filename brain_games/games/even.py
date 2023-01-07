import random


def build_qlist():
    qlist = []
    for i in range(3):
        random_int = random.randint(1, 100)
        qlist.append(random_int)
    return qlist


def calc_function(list_for_eval):
    rlist = []
    for elem in list_for_eval:
        result = 'yes' if elem % 2 == 0 else 'no'
        rlist.append(result)
    return rlist
