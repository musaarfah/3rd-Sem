def gcd(n1,n2):
    # if n1%n2==n1:
    #     return n1
    # elif n2%n1==n2:
    #     return n2
 

    # if n1%n2==0 and n2%n2==0:
    #     return n2
    # return gcd(n1-1,n2-1)

    if n2==0:
        return n1
    
    return gcd(n2,n1%n2)

print(gcd(18,6))