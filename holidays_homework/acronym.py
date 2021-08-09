'''
Author: Matteo Lamberti
Date: 02/08/21

Help generate some jargon by writing
a program that converts a long name
like Portable Network Graphics
to its acronym (PNG).
'''

def main():
    phrase=input("Enter a phrase: ")
    word_list=phrase.split(" ")
    acronym=""
    for word in word_list:
        acronym+=word[0]
    print(acronym)

if __name__=="__main__":
    main()