import random


def build_qlist():
    qlist = []
    deleted_elem_list = []
    for i in range(3):
        step = random.randint(-10, 10)
        first_number = random.randint(1, 10)
        progression = [str(x) for x in
                       range(first_number, first_number + step * 10, step)]
        index = random.randint(1, len(progression) - 1)
        deleted_elem_list.append(int(progression[index]))
        progression[index:index + 1] = ['..']
        res_sing = ' '.join(progression)
        qlist.append(res_sing)
    return qlist, deleted_elem_list
