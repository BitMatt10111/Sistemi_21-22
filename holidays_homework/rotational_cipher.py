'''
Author: Matteo Lamberti
Date: 02/08/21

Help generate some jargon by writing
a program that converts a long name
like Portable Network Graphics
to its acronym (PNG).
'''

def cript(cod,key):
    fin=""
    for k in range(len(cod)):
        if(ord(cod[k])+key>ord('z')):
            fin+=chr(96+(ord(cod[k])+key-ord('z')))
        else:
            fin+=chr(ord(cod[k])+key)
    return fin

def decript(cod,key):
    fin=""
    for k in range(len(cod)):
        if(ord(cod[k])-key<ord('a')):
            fin+=chr(123-(ord('a')-(ord(cod[k])-key)))
        else:
            fin+=chr(ord(cod[k])-key)
    return fin

def main():
    key=int(input("ROT-"))
    word=input("Enter a word to be cripted: ")
    print(cript(word,key))
    print(decript(cript(word,key),key))

if __name__=="__main__":
    main()