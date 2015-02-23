def multi (n,m):
    for i in range(1,m):
        print ('{}{}_=_{}{}_*_{}'.format('_'*(len(str(m*n))-len(str(i*n))),i*n,'_'*(len(str(m))-len(str(i))), i, n))

if __name__ == '__main__':
    #inp = raw_input('Intup 2 numbers :').split(',')
    #multi(int(inp[0]),int(inp[1]))
    multi(7,311)