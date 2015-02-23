def neighbor (size, x , y):
    res = []
    if x-1 >= 0:    res.append((x-1, y,))
    if x+1 < size:  res.append((x+1,y,))
    if y-1 >= 0:    res.append((x, y-1,))
    if y+1 < size:  res.append((x,y+1,))
    return res

if __name__ == '__main__':
    size = 4
    labirint = [[1,0,0,0],[1,0,1,1],[1,0,0,1],[1,1,1,1]]
    start = (0,0,)
    finish = (1,2,)
    step = 1
    plan = []
    plan.append(start)
    flag =0
    while len(plan) != 0:
        step += 1
        current = plan.pop()
        labirint[current[0]][current[1]] = step
        for nei in neighbor(size, current[0], current[1]):
            if nei == finish:
                print 'Find exit!'
                flag =1
            if labirint[nei[0]][nei[1]] == 1: # and labirint[nei[0]][nei[1]] < step:
                labirint[nei[0]][nei[1]] = step
                plan.append(nei)
        if flag == 1: break

    if labirint[finish[0]][finish[1]] == 1:
        print 'There is NO EXIT!'
    else:
        print 'Len Way = %d' %(labirint[finish[0]][finish[1]]-1)
    for raw in labirint:
        print raw



