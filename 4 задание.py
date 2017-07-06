def Zad(n):
    bi=[]
    o=n.split(' ')
    for m in o:
        if m not in bi:
            bi.append(m)
    print(bi)
