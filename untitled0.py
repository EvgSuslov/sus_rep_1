#Write a program to determine if the two given numbers
# are coprime. A pair of numbers are 
#coprime if their greatest shared factor is 1.

#The inputs will always be two positive integers between 2 and 99.

def are_coprime(n,m):
    b=[]
    c=[]
    for i in range(1, 100):
        if n % i == 0:
            b.append(i)
    for j in range(1, 100):
        if m % j == 0:
            c.append(j)
    result = list(set(b) & set(c))

    for number in result:
        a = 0
        if number >= a:
            a = int(number)
    if number == 1:
        return True
    else:
        return False
    
"аоаоао"
