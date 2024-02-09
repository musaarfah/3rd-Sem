



# def palindrome(str):
#     a=[]
#     b=[]
#     for i in range(len(str)):
#        a.append(str[i])
#     for i in range(len(str)-1,-1,-1):
#        b.append(str[i])
#     for i in range(len(a)):
#        if a[i]!=b[i]:
#           return False
#     return True

# print(palindrome('madam'))

def palin(str):
    if len(str)==1:
        return True
    if str[0]!=str[-1]:
        return False
    else:
        str=str[1:-1]
        return palin(str)

print(palin('madam'))