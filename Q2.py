
# s='juliuscaesar'
# r=''
# for i in range(len(s)-1,-1,-1):
#     r+=s[i]




def reverse_str(str):
    if len(str)== 1:
        return str[0]
    
    return str[-1]+reverse_str(str[:-1])

print(reverse_str('fire'))