'''
Author: Matteo Lamberti
Date: 02/08/21

Determine if a sentence is a pangram.
A pangram is a sentence using every
letter of the alphabet at least once.
'''

import string

def main():
    phrase=input("Enter a phrase: ")
    alphabet=string.ascii_lowercase
    l_alphabet=[]
    for letter in alphabet:
        l_alphabet.append(letter)
    for letter in phrase:
        if letter in l_alphabet:
            l_alphabet.remove(letter)
    if len(l_alphabet)==0:
        print("The phrase is a pangram")
    else:
        print("The phrase is not a pangram")

if __name__=="__main__":
    main()