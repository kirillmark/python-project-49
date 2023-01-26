import random


def build_qlist():
    qlist = []
    for i in range(3):
        step = random.randint(1, 20)
        first_number = random.randint(1, 10)
        progression = [str(x) for x in
                       range(first_number, first_number + step * 10, step)]
        index = random.randint(0, len(progression) - 1)
        progression[index] = '..'
        res_sing = ' '.join(progression)
        qlist.append(res_sing)
    return qlist


def build_alist(list_for_eval):
    rlist = []
    for elem in list_for_eval:
        num_l = elem.split()
        i = num_l.index('..')
        if i == 0:
            i_num = int(num_l[1]) - (int(num_l[4]) - int(num_l[3]))
        elif i == len(num_l) - 1:
            i_num = int(num_l[-2]) + (int(num_l[4]) - int(num_l[3]))
        else:
            i_num = (int(num_l[i - 1]) + int(num_l[i + 1])) // 2
        rlist.append(i_num)
    return rlist
