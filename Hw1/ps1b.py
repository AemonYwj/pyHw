# -*- coding: UTF-8 -*- 

import linecache as lc
from pickle import FALSE, TRUE
import random
from signal import SIG_DFL

from numpy import true_divide


#words = open('hangmanDict.txt','r')

rand = random.randrange(1,274926)

line = lc.getline('hangmanDict.txt',rand)

print("Guess what letter is in the word.")
flag = False

while True:
    char = input("My guess is the letter: ")
    for ch in line:
        if ch == char:
            print("You are RIGHT!")
            flag = True
            break
    if flag == True:
        break
    print("So close! Please gusses again.")

print ("The word is",line)


    
    

