string = 'sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list'
#string = 'aaa ababa sadjskafh jutgior kldfnjiii'
splt = string.split()
tup = zip(splt, [set(i) for i in splt])
tup.sort(key = lambda x: len(x[1]))
result = []
for s in tup:
    result.append(s[0])

print ' '.join(result)