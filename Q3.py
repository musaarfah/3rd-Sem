

# def binary_search(l,t):
#     mid=len(l)//2

#     if l[mid]==t:
#         return l[mid]
    
#     elif t>l[mid]:
#         for i in range(mid+1,len(l)):
#             if l[i]==t:
#                 return l[i]
#     elif t<l[mid]:
#         for i in range(mid+1):
#             if l[i]==t:
#                 return l[i]
#     else:
#         return False
    
# print(binary_search(l,10))

# def binary_search(l,t):
#     left=0
#     right=len(l)

#     while left<=right:
#         mid=(left+right)//2

#         if l[mid]==t:
#             return mid
        
#         elif l[mid]<t:
#             left=mid+1

#         elif l[mid]>t:
#             right=mid-1
    
#     return  -1
           

# print(binary_search(l,3))


l=[2,4,5,6,7,8,9,10,12]


def binary_search(l,s,e,t):
    mid=(s+e)//2

    if l[mid]==t:
        return mid
    
    elif l[mid]<t:
        return binary_search(l,mid+1,e,t)
    
    elif l[mid]>t:
        return binary_search(l,s,mid-1,t)
    
    else:
        return -1
    
print(binary_search(l,0,len(l),6))