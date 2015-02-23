def konggen (start, a, c, m):
    while True:
        n = a*start +c
        yield n%m
        start = n


if __name__ == '__main__':
    start = 7
    a = 7
    c = 7
    m = 10
    sample = 6
    for s in konggen(start,a ,c, m):
        if s == sample:
            print s
            print 'YES'
            break
        else:
            print s
            print 'NO'
