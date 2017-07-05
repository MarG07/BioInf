from pprint import pprint
with open(r"C:\Users\marin\Downloads\small.fastq") as inp:
    for line in inp:
        print(line)
        l=line.strip()
with open(r"C:\Users\marin\Downloads\small_ref.fa") as f:
    first=true
    ref=''
    ref_name=''
    for line in f:
        print(line)
def Score(o,p):
    if o == p:
        return 1
    if o != p:
        return -1
    
def align(s,t):
    xs = []
    for i in range(0, len(s) + 1):  
        r=[]
        for j in range(0, len(t)+1):
            r.append(0)
        xs.append(r)
        
    for j in range(0, len(t) + 1):
        xs[0][j]=0
        
    for i in range(0, len(s) + 1):
        xs[i][0]=0
    e=0
    d = 0
    f = 0
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            a = xs[i-1][j-1] + Score(s[i-1],t[j-1])
            b = xs[i-1][j] + Score(s[i-1],'-')
            c = xs[i][j-1] + Score('-',t[j-1])
            if a>b and a>c and a > 0:
                xs[i][j] = a
            elif b>c and b > 0 :
                xs[i][j] = b
            elif b<c and c > 0:
                xs[i][j] = c
            else:
                xs[i][j] = 0

            if xs[i][j] > e :
                e=xs[i][j]
                d=i
                f=j
                
    i = d
    j = f
    sa = ''
    ta = ''
    while xs[i][j]>0:
        if i > 0 and j > 0 and xs[i-1][j-1] + Score(s[i-1],t[j-1]) == xs[i][j]:
            sa=s[i-1] + sa
            ta=t[j-1] + ta
            i=i-1
            j=j-1
        if i > 0 and xs[i-1][j] + Score(s[i-1],'-') == xs[i][j]:
            
            sa=s[i-1] + sa
            i=i-1
            ta='-' + ta 
        if j > 0 and xs[i][j-1] + Score('-',t[j-1]) == xs[i][j]:
            
            ta=t[j-1] + ta
            j=j-1    
            sa='-' + sa
            
    print(sa)
    print(ta)
    
    pprint(xs)

    
