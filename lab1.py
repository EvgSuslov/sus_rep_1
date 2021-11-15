#метод шифровки перестановка
import sys
import numpy as np
min_n=3 #Минимальное число для алгоритма деления 
k=0 #для определения TRUE FALSE на простое
print("enter messege (max 14)")
s = input()
print(len(s)) #считает символы
len_ar=(len(s))
for i in range(2, len_ar // 2+1): #проверяет простое ли число и останваливает скрипт если да
    if len_ar % i == 0:
        k+=1
if (k!=0):
    print(str(len_ar)+' not a simple')
else:
    print(str(len_ar) + ' is simple true')
    sys.exit()                                   #тут в строке надо добавить лишний символ в конце но я хз как по этому прерывание
while len_ar % min_n != 0:                       # while true пока остаот от деленеия не равен 0
    if len_ar % min_n == 0:                      # если остаток от деления равен 0 
        print ('') 
        break
    elif len_ar % min_n != 0: 
         min_n+=1                          # если остаток от деления не равен 0
else:  
    rng = list(range(1, min_n+1))
    print(rng)                                # выражение while FALSE

print(s[:min_n], s[min_n:])
st1 = s[:min_n]
st2 = s[min_n:]
rng = list(range(1, min_n+1))
print (str(rng) + '\n'+ str(list (st1)) +'\n' + str(list (st2)))

#тут крч надо сдела так чтоб 3 массива друг с другом сочлинялись 
#во что то типо ('a', 'b', 3)
#или по итогу сделать чтоб массив был ключом я хз

#print([rng[i^1] for h in range(1, min_n)])

#тут у нас должна быть сортировака по 1 шаблону / 
#всех массивов
