"""def show(n):
    print(n)
    if n == 0:
        return
    show(n-1)


show(4)


def fac(n):
    if n == 0 or n == 1:
        return 1
    return fac(n-1)*n


print(fac(4))



def clu_sum(n):

    if n == 0:
        return 0
    return clu_sum(n-1)+n


sum = clu_sum(5)
print(sum)
"""


def print_list(list, indx=0):
    if indx == len(list):
        return
    print(list[indx])
    print_list(list, indx+1)


f = [1, 2, 3, 4, 5, 6, 7]
print_list(f)
