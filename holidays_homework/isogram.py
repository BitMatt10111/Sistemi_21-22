'''
Name: Matteo Lamberti
Date: 28/07/21

Determine if a word or phrase is an isogram.
An isogram (also known as a "nonpattern word")
is a word or phrase without a repeating letter,
however spaces and hyphens are allowed to
appear multiple times.
'''

def main():
    s=input("Enter a word: ")
    check_s=[]
    isogram=True
    for letter in s:
        for check_letter in check_s:
            if letter == check_letter:
                isogram=False
        check_s+=letter
    if isogram:
        print("It's an isogram")
    else:
        print("It's not an isogram")

if "__main__"==__name__:
    main()