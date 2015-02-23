def maxsubstr(string):
    maxlen = len(set(string))
    for i in range(2,len(string)):
        for j in range(len(string)-i):
            if len(string[j:j+i]) == len(set(string[j:j+i])):
                result = string[j:j+i]
    return result

if __name__ == '__main__':
    instr = 'qweqweASDFGHASDFGASasdfghas123'
    print maxsubstr(instr)