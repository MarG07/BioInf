def mfib(n):
    fibn = [1, 1]
    for i in range(2, n + 1):
        fibn.append(fibn[i - 1] + fibn[i - 2])
    return fibn

def Fib(n,m):
    xs = mfib(m)
    xs[-1] -= 1
    for k in range(m +1 , n + 1):
        xs.append(xs[k - 1] + xs[k - 2] - xs[k - m-1])
    return xs[n-1]

for i in range(1, 9):
    print(Fib(i, 3))



