def polska(string):
    res = []
    string = string.split()
    for el in string:
        if el.isdigit():
            res.append(el)
        elif el in ['+','-','*','/']:
            try:
                y = res.pop()
                x = res.pop()
                res.append(str(eval(x+el+y)))
            except IndexError:
                print  'ERROR'
                break
    return res.pop()

if __name__ == '__main__':
    string = '234 345 456 + + 5 /'
    print polska(string)
