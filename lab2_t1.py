# def dectooct(n):
#     if n==0:
#         return
#     dectooct(n//8)
#     print(n%8,end=' ')


# dectooct(16)

def dectoBin(n):
    if n==0:
        return
    print(n%2,end=' ')
    dectoBin(n//2)



dectoBin(38)