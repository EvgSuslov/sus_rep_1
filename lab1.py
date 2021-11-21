#метод шифровки перестановка
import sys
import random

min_n=3 #Минимальное число для алгоритма деления 
k=0 #для определения TRUE FALSE на простое
print("введите сообщение")
s = input()
print('кол-во букв в тексте' + str(len(s))) #считает символы
len_ar=(len(s))
for i in range(2, len_ar // 2+1): #проверяет простое ли число и останваливает скрипт если да
    if len_ar % i == 0:
        k+=1
if (k!=0):
    print(str(len_ar)+' это простое число')
else:
    print(str(len_ar) + ' это не простое число'+ '\n' +'Введите иное сообщение')
    sys.exit()                                   #тут в строке надо добавить лишний символ в конце но я 
                                                    #прерываниемамаамама
while len_ar % min_n != 0:                       # while true пока остаот от деленеия не равен 0
    if len_ar % min_n == 0:                      # если остаток от деления равен 0 
        print ('') 
        break
    elif len_ar % min_n != 0: 
         min_n+=1                          # если остаток от деления не равен 0
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
