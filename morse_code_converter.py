#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#create dict for key value pairs
code_cvt = {"A": ".-",
"B": "-...",
"C": "-.-.",
"D": "-..",
 "E": ".",
 "F": "..-.",
 "G": "--.",
 "H": "....",
 "I": "..",
   "J": ".---",
   "K": "-.-",
   "L": ".-..",
   "M": "--",
   "N": "-.",
   "O": "---",
   "P": ".--.",
   "Q": "--.-",
   "R": ".-.",
  "S": "...",
  "T": "-",
   "U": "..-",
   "V": "...-",
   "W": ".--",
 "X": "-..-",
  "Y": "-.--",
  "Z": "--..",
  " ": "   ",
  "1": ".----",
  "2": "..---",
   "3": "...--",
   "4": "....-",
 "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
   "0": "-----"
 }

while True:
    inp = input("enter the sentence you want to convert: ")
    inp = inp.upper()
    a = ""
    for letter in inp:
        if letter in code_cvt.keys():
            b = code_cvt[letter]
            a = a + b
        else:
            print('enter valid input')
    print(a)
    x = 0
    while x != 1:
        sep = input("do you want to enter another sentence? (Y/N): ")
        sep = sep.upper()
        if sep == 'Y' or sep == 'N':
            x = 1
        else:
            print('enter valid format')
            x = 0
    
    if sep == 'N':
        break
    elif sep == 'Y':
        continue
   
               
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            