'''
Name: Matteo Lamberti
Date: 30/7/21

The diamond kata takes as its input a letter,
and outputs it in a diamond shape. Given a
letter, it prints a diamond starting with
'A', with the supplied letter at the widest point.
'''

import string

def main():
    letter=input("Enter a letter (lowercase plz): ")
    center_index=string.ascii_lowercase.index(letter)
    space=""
    mid_space=" "
    for _ in range(center_index):
        space+=" "
    for i in range(center_index+1):
        if i==0:
            print(f"{space}{string.ascii_lowercase[i]}")
        else:
            print(f"{space}{string.ascii_lowercase[i]}{mid_space}{string.ascii_lowercase[i]}")
            mid_space+="  "
        space=space[1:]
    space=" "
    mid_space=mid_space[4:]
    for i in range(center_index):
        if i==center_index-1:
            print(f"{space}{string.ascii_lowercase[center_index-i-1]}")
        else:
            print(f"{space}{string.ascii_lowercase[center_index-i-1]}{mid_space}{string.ascii_lowercase[center_index-i-1]}")
            mid_space=mid_space[2:]
        space+=" "

if "__main__"==__name__:
    main()