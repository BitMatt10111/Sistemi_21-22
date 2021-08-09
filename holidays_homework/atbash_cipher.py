'''
Author: Matteo Lamberti
Date: 20/07/21

The Atbash cipher is a simple substitution
cipher that relies on transposing all the
letters in the alphabet such that the resulting
alphabet is backwards.
'''
import string

def encoding(p,a):
    fp=""
    for p_letter in p:
        if p_letter in a:
            for i,a_letter in enumerate(a):
                if p_letter==a_letter:
                    fp+=a[-(i+1)]
        else:
            fp+=p_letter
    return fp

def decoding(p,a):
    fp=""
    for p_letter in p:
        if p_letter in a:
            for i,a_letter in enumerate(a):
                if p_letter==a_letter:
                    fp+=a[i+1]
        else:
            fp+=p_letter
    return fp

def main():
    alphabet=string.ascii_lowercase
    final_phrase=""
    phrase=input("Enter a phrase to encrypt: ")
    while(True):
        opz=input("Select encoding typing: 0 or decoding typing: 1 --> ")
        if(opz=="0"):
            final_phrase=encoding(phrase,alphabet)
            break
        elif(opz=="1"):
            final_phrase=encoding(phrase,alphabet)
            break
        else:
            print("Error: enter a valid value")
    print(final_phrase)

if __name__=="__main__":
    main()