# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 18:49:59 2021

@author: Fox
"""

'''
ПСЧ
'''
b = 6

import numpy as np
A = 5
C = 3
T = 7
M = 2 ** b

def get_next(t):
    return (A * t + C) % M

def cipher(text, t):
    gamma = []
    mes = []
    
    smesh = ord('а') - 1 # Потому что мы считаем по позиции а алфавите, а не по позиции в ASCii
    
    text = text.lower().replace(' ', '') # Потому что мы не шифруем знаки препинания, и нам нафиг не нужен регистр
    for i in text:
        mes.append(ord(i) - smesh)
        t = get_next(t)
        gamma.append(t)
    gamma = np.array(gamma) # Потому что мне впадлу писать обход по двум массивам и \
    mes = np.array(mes) # делать математику на медленном питоне, прекомпилированный numpy поможет
    
    ans = (gamma ^ mes) % 32 # величина алфавита у нас 32
    
    print(f'Гамма: {gamma}')
    print(f'Сообщение: {mes}') # Потому что дебаг
    print(f'Шифрованное сообщение: {ans}') 
    
    mes = ''
    for i in ans:
        if i == 0:
            i = 32 # потому что у нас "а" равно 1, а не 0, как у всех нормальных программистов, оттого "я" == 32 тупит
        mes += chr(i + smesh)
    return mes
    
message = input('Введите сообщение на русском языке без ё: ') or 'раз два три четыре пять'
ciph = cipher(message, T)
print(ciph)
print(cipher(ciph, T)) # Потому что симметричный код


