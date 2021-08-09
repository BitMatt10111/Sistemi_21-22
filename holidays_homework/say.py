'''
Name: Matteo Lamberti
Date: 01/08/21

Given a number from 0 to 9999 spell out that number in English.
'''

one_digit=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
two_digits=["","ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
multiples_of_ten=["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
three_digits="hundred"
four_digits="thousand"

def say(number,number_s):
    if len(number_s)==1:
        ret=f_one_digit(number)
    if len(number_s)==2:
        ret=f_two_digits(number)
    if len(number_s)==3:
        ret=f_three_digits(number)
    if len(number_s)==4:
        ret=f_four_digits(number)
    return ret

def f_one_digit(n):
    return one_digit[n]

def f_two_digits(n):
    if n%10==0 and n!=10:
        return multiples_of_ten[int(n/10)]
    elif n<20:
        return two_digits[int(n%10)+1]
    else:
        output=""
        output+=multiples_of_ten[int(n/10)]+"-"
        output+=f_one_digit(n%10)
        return output

def f_three_digits(n):
    output=""
    if n%100==0:
        output+=f_one_digit(int(n/100))+" "
        output+=three_digits
    elif int((n%100)/10)==0:
        output+=f_one_digit(int(n/100))+" "
        output+=three_digits+" and "
        output+=f_one_digit(n%100)
    else:
        output+=f_one_digit(int(n/100))+" "
        output+=three_digits+" and "
        output+=f_two_digits(n%100)
    return output

def f_four_digits(n):
    output=""
    if n%1000==0:
        output+=f_one_digit(int(n/1000))+" "
        output+=four_digits
    elif int(((n%1000)%100)/10)==0:
        output+=f_one_digit(int(n/1000))+" "
        output+=four_digits+" and "
        output+=f_one_digit(n%1000)
    elif int((n%1000)/100)==0:
        output+=f_one_digit(int(n/1000))+" "
        output+=four_digits+" and "
        output+=f_two_digits((n%1000)%100)
    else:
        output+=f_one_digit(int(n/1000))+" "
        output+=four_digits+" and "
        output+=f_three_digits((n%1000))
    return output

def main():
    while True:    
        number_s=input("Enter a number: ")
        number=int(number_s)
        if number>=0 and number<=9999:
            break
    print(say(number,number_s))

if __name__=="__main__":
    main()