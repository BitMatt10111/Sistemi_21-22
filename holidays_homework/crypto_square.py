'''
Author: Matteo Lamberti
Date: 02/08/21

Implement the classic method for composing
secret messages called a square code.
Given an English text, output the
encoded version of that text. First, the
input is normalized: the spaces and punctuation
are removed from the English text and the message is downcased.
Then, the normalized characters are broken
into rows. These rows can be regarded as
forming a rectangle when printed with intervening newlines.
'''

char_to_be_deleted=['.',',',';',':','-',"'",' ','"']
from math import ceil,sqrt

def main():
    phrase=input("Enter a phrase to be crypted: ")
    normalized=""
    for letter in phrase:
        if not letter in char_to_be_deleted:
            normalized+=letter
    c=ceil(sqrt(len(normalized)))
    r=round(sqrt(len(normalized)))
    rows_list=[]
    for i in range(0,len(normalized),c):
        rows_list.append(normalized[i:c+i])
    crypted_phrase=""
    for i in range(c):
        for row in rows_list:
            if not i >= len(row):
                crypted_phrase+=row[i]
    print(f"The crypted phrase is: {crypted_phrase}")

if __name__=="__main__":
    main()