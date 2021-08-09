'''
Author: Matteo Lamberti
Date: 20/07/21

The ISBN-10 format is 9 digits (0 to 9) plus one
check character (either a digit or an X only).
In the case the check character is an X, this
represents the value '10'. These may be communicated
with or without hyphens, and can be checked for their
validity by the following formula:
(x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
'''

import string

def main():
    isbn=input("Enter an ISBN to validate: ")
    tot=0
    factor=10
    for value in isbn:
        if value in string.digits:
            tot+=int(value)*factor
            factor-=1
        if value == "X":
            tot+=10*factor
    if tot%11==0:
        print("The ISBN is valid")
    else:
        print("The ISBN is not valid")

if __name__=="__main__":
    main()