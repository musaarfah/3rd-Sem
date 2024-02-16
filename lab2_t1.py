def dectooct(n):
    if n==0:
        return
    dectooct(n//8)
    print(n%8,end=' ')


dectooct(250)