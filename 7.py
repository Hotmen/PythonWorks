def strrepeat (str):
    for i in range(1,len(str)):
        if str[:i]*(len(str)/i) == str :
            return str[:i] , len(str)/i

if __name__ == '__main__':
    s = 'abcabcabcabc'
    print strrepeat(s)