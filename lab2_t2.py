def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True
    
def string_check(str):
    if len(str)==0:
        return
    if len(str)==1:
        if int(str[0])%2==0:
            return True

    if int(str[0])%2==0 and isPrime(int(str[1])):
        return True
    
    if len(str)!=1:
       string_check(str[2:])

def check_good_string(str):
    if string_check(str):
        print('Good String')

    else:
        print('Not Good String')

check_good_string('2387')
