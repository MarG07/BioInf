def Fib(n):
    xs = [0, 1, 1]

    for k in range(3, n + 1):
        xs.append(xs[k - 3] + xs[k - 2])

    return xs[n]

print(Fib(5))



