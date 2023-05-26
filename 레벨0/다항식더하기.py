def solution(poly):
    p = poly.split()
    list = []
    a = 0
    b = 0
    for i in p:
        if "x" in i:
            list.append(i)
        elif i != "+":
            a += int(i)

    for i in list:
        if i == "x":
            b += 1
        else:
            b += int(i[:-1])
    if a == 0: 
        if b == 1:
            return "x"
        return str(b) + "x"
    elif b == 1:
        return "x + " + str(a)
    elif b == 0:
        return str(a)
    else:
        return str(b) + "x + " + str(a)