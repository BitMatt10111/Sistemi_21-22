'''
Name: Matteo Lamberti
Date: 01/08/21

Given an input text output it transposed.

Roughly explained, the transpose of a matrix:

ABC
DEF

is given by:

AD
BE
CF

Rows become columns and columns become rows.
'''

def main():
    strings=[]
    while True:
        s=input("Enter a string (same lenght): ")
        strings.append(s)
        ans=input("It's enough (write 'yes' to stop)? ")
        if ans=="yes" or ans=="YES":
            break
    new_strings=[]
    for j,s in enumerate(strings):
        for i,letter in enumerate(s):
            if j==0:
                new_strings.append(letter)
            else:
                new_strings[i]+=letter
    for string in new_strings:
        print(string)

if __name__=="__main__":
    main()