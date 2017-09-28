def divisble_sublist(list1, d1, d2):
    byd1 = any(list1 % d1 == 0 for i in d1)
    byd2 = any(list1 % d2 == 0 for i in d2)
    list2 = byd1 + byd2
    return list2
