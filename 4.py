def krug (circle, points):
    result = False
    for point in points:
        print point
        if ((point[0]-circle[0])**2 + (point[1]-circle[1])**2) == circle[2]**2:
            result = True
        else:
            return False
    return result

if __name__ == '__main__':
    circle = []
    points = []
    a = raw_input('Input center and radius througth "," :')
    for i in a.split(','):
        circle.append(int(i.strip()))
    a = raw_input('Input points througth "," :')
    a=a.split(',')
    print type(a)
    for i in range(0,len(a)-1,2):
        points.append([int(a[i].strip()), int(a[i+1].strip())])
    print circle
    print points
    print krug (circle, points)