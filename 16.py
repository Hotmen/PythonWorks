if __name__ == '__main__':
    data = [5, 3, 6, 1, 1, 2, 3, 4, 7, 5, 5, 7, 1, 1, 4, 6, 3, 4, 7, 4, 2]
    step = 4
    res = data[:step]
    for i in range(step, len(data)):
        res.append(data[i]+min(res[-step:]))
    print res
    print res[-1]
