'''
Name: Matteo Lamberti
Date: 01/08/21

Compute the prime factors of a given natural number.
'''

def main():
    number=int(input("Enter a number: "))
    factors=[]
    while True:
        factor=2
        while number%factor!=0:
            factor+=1
            if factor==number:
                break
        if factor==number or number==1:
            factors.append(int(number))
            break
        factors.append(factor)
        number=number/factor
    print(factors)


if __name__=="__main__":
    main()