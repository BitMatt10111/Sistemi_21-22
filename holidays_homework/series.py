'''
Name: Matteo Lamberti
Date: 31/7/21

Given a string of digits,
output all the contiguous substrings
of length n in that string in
the order that they appear.
'''

def main():
    string=input("Enter a string: ")
    subs_length=int(input("Enter the sub string length: "))
    i=0
    while True:
        print(string[i:i+subs_length])
        i+=1
        if i+subs_length>len(string):
            break

if "__main__"==__name__:
    main()