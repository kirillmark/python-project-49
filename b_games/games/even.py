def build_alist(list_for_eval):
    rlist = []
    for elem in list_for_eval:
        result = 'yes' if elem % 2 == 0 else 'no'
        rlist.append(result)
    return rlist
