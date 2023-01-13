import random


def build_qlist():
    qlist = []
    for i in range(3):
        step = random.randint(1, 20)
        first_number = random.randint(1, 10)
        progression = [str(x) for x in
                       range(first_number, first_number + step * 10, step)]
        index = random.randint(0, len(progression) - 1)
        progression[index:index + 1] = ['..']
        res_sing = ' '.join(progression)
        qlist.append(res_sing)
    return qlist


def build_alist(list_for_eval):
    rlist = []
    for elem in list_for_eval:
        p_list = elem.split()
        q_num = 0
        for i in range(len(p_list)):
            if p_list[i] == '..' and (i != 0 and i != len(p_list) - 1):
                q_num = (int(p_list[i + 1]) + int(p_list[i - 1])) // 2
            elif p_list[i] == '..' and i == 0:
                q_num = int(p_list[1]) - (int(p_list[4]) - int(p_list[3]))
            elif p_list[i] == '..' and i == len(p_list) - 1:
                q_num = int(p_list[-2]) + (int(p_list[4]) - int(p_list[3]))
        rlist.append(q_num)
    return rlist
