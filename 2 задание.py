#def Slovar(n):
 #   for i in range(n):               Это тоже решение!
  #      l=i**2
   #     print(i, ':', l)
def sl(n):
    o = {y: y ** 2 for y in range(1, n)}
    return o
