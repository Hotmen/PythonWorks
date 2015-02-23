def mostword(text):
    dic = {}
    mass = text.split()
    for word in set(mass):
        if dic.has_key(mass.count(word)):
            dic[mass.count(word)].add(word)
        else:
            dic[mass.count(word)] = {word}
    if len(dic[max(dic.keys())]) > 1:
        print '---'
    else:
        print dic[max(dic.keys())].pop()



if __name__ == '__main__':
    text = 'Sed tempus ipsum quis eros tempus lacinia Cras finibus lorem ut lacinia egestas nunc nibh iaculis est convallis tincidunt mi mi sed nisl Sed porttitor aliquam elit ullamcorper tincidunt arcu euismod quis Mauris congue elit suscipit leo varius facilisis Cras et arcu sodales laoreet est vitae pharetra orci Integer eget nulla dictum aliquet justo semper molestie neque Maecenas bibendum lacus tincidunt auctor varius purus felis ullamcorper dui et laoreet ligula ex et risus Donec eget fringilla nibh Cras congue tincidunt accumsan Maecenas euismod eleifend elit ut rhoncus tortor sodales a Cras egestas finibus lorem non tempor tincidunt aera'
    mostword(text)