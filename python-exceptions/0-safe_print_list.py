#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    c = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            c += 1
        except IndexError:
            break
    print()
    return c

'''
my_list = [1, 2, 3, 4, 5]
print(safe_print_list(my_list, 2))
'''
