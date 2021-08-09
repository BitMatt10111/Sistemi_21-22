'''
Author: Matteo Lamberti
Date: 01/08/21

Given a string representing a matrix of numbers,
return the rows and columns of that matrix.
'''

def main():
    lines=[]
    while True:
        row=input("Enter a candidate (same lenght): ")
        lines.append(row)
        ans=input("It's enough (write 'yes' to stop)? ")
        if ans=="yes" or ans=="YES":
            break
    digits=[]
    for row in lines:
        digits_row=[]
        for digit in row:
            digits_row.append(digit)
        digits.append(digits_row)
    space="    "
    output=space
    for i in range(len(digits[0])):
        output+=f"{i+1} "
    print(f"{output}\n")
    for i,row in enumerate(digits):
        output=f"{i+1}{space[1:]}"
        for element in row:
            output+=f"{element} "
        print(output)

        

        

if __name__=="__main__":
    main()