def dirlist(name):
    for n in dir(name):
        if n[0] != '_':
            print n

if __name__ == '__main__':
    while True:
        name = raw_input('Input anything :')
        dirlist(name)
