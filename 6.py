def rndcort(lst):
    return lst[-2::-2] + lst[1::2]

if __name__ == '__main__':
    lst = ['0', 1, 2, '3', 4, 5, '6', 7, 8, '9', 10, 11]
    print rndcort(lst)