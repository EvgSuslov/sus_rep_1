'''  
the permutation cipher
    task - random shuffle + code of shuffle
        working as like 
    in input random string ex. ('secret place')
    if simple - than make another string
                        .add in v.2  - if simple + (' ' at the end)
    return ciphered sting  + [21365]
'''
import sys
import random

min_n=3 #minimal sep. for string
k=0 #mor simple of not
print("input string: \n") 
s = input()
print('len of string is: ' + str(len(s))) 
len_ar=(len(s))
for i in range(2, len_ar // 2+1): #if simple - than do anoter
    if len_ar % i == 0:
        k+=1
if (k!=0):
    print(str(len_ar)+': is simple')
else:
    print(str(len_ar) + 'not simple '+ '\n' +'Enter another one')
    sys.exit()                                    
                                                    
while len_ar % min_n != 0:                       
    if len_ar % min_n == 0:                      
        print ('') 
        break
    elif len_ar % min_n != 0: 
         min_n+=1                          
else:  
    rng = list(range(0, min_n))
    
print('this is your key = ' )
random.shuffle(rng)
print(rng)
 
def encode(text, key):
    n = len(text)
    m = len(key)
    p = ''
    q = 0
 
    while q < n:
        p += ''.join(text[q+x] for x in key)
        q += m
 
    return p
 
print(encode(s,rng))
"fffff"