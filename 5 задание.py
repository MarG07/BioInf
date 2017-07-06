def Fun(n):
    bi=[]
    ci=[]
    p=n.split(', ')
    for m in p:
        o=m.split(' ')
        bi += [o[0]]*int(o[1])
    bi.sort()
    print(', '.join(bi))
