def secmax(lst):
    return sorted(lst)[-2]

if __name__ == '__main__':
    s = []
    a = raw_input('Input list througth "," :')
    for i in a.split(','):
        s.append(i.strip())
    print s
    print secmax(s)