from math import *
def gen (start, stop):
    for i in range (start, stop):
        yield i

if __name__ == '__main__':
    str = '(x**5+1)/(factorial(x)-720)'
    start = -10
    stop = 10
    res = []
    for x in gen(start, stop):
        try:
            res.append(eval(str))
        except:
            pass
    print max(res), min(res)