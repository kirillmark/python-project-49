import random


def isprime(number):
    d = 2
    while d * d <= number and number % d != 0:
        d += 1
    return d * d > number


def build_qlist():
    qlist = []
    for i in range(3):
        random_int = random.randint(1, 100)
        qlist.append(random_int)
    return qlist


def build_alist(list_for_eval):
    rlist = []
    for elem in list_for_eval:
        result = 'yes' if isprime(elem) else 'no'
        rlist.append(result)
    return rlist
