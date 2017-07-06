def Zad(n):
    a = 0
    m = 0
    for a in range(n):
        if a % 5==0:
            m += a
        elif a % 3==0:
            m += a
    return m
