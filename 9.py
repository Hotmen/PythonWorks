from itertools import combinations

lst = [1,2,3,4,5,6,7,10,30,44,73,1223,55,576,3]
maximum = 10
number = 211
stop = 0

for i in range(maximum):
    iterator = combinations(lst, i)
    for pair in iterator:
        if sum(pair) == number:
            stop = 1
            print 'YES ', pair
            break
    if stop == 1:
        break
if stop == 0:
    print 'NO'