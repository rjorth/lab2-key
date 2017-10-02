def divisible_sublist(list1, d1, d2):
    d1_test = [x for x in list1 if x % d1 == 0]
    d2_test = [x for x in list1 if x % d2 == 0]
    list2 = d1_test + d2_test
    return list2
