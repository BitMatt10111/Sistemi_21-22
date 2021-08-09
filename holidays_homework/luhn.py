'''
Name: Matteo Lamberti
Date: 28/07/21

Given a number determine whether or not it is valid per the Luhn formula.
Strings of length 1 or less are not valid. Spaces are allowed in the input,
but they should be stripped before checking. All other non-digit characters
are disallowed.
Example 1: valid credit card number
4539 1488 0343 6467
The first step of the Luhn algorithm is to double every second digit,
starting from the right. We will be doubling
4_3_ 1_8_ 0_4_ 
If doubling the number results in a number greater than 9 then subtract
9 from the product. The results of our doubling:
8569 2478 0383 3437
Then sum all of the digits:
8+5+6+9+2+4+7+8+0+3+8+3+3+4+3+7 = 80
If the sum is evenly divisible by 10, then the number is valid.
This number is valid!
'''

def main():
    while True:
        number=input("Enter a number to be validate: ")
        if number.isnumeric():
            break
    digits_list=[]
    for digit in number:
        digits_list.append(int(digit))
    index=-2
    while True:
        double_digit=digits_list[index]*2
        if double_digit >= 10:
            double_digit-=9
        digits_list[index]=double_digit
        print(double_digit)
        if digits_list[index]==digits_list[0] or digits_list[index]==digits_list[1]:
            break
        index-=2
    if sum(digits_list) % 10==0:
        print("It's valid")
    else:
        print("It's not valid")


if "__main__"==__name__:
    main()
        