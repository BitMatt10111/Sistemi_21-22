'''
Author: Matteo Lamberti
Date: 23/07/21

Reverse a string
For example: input: "cool" output: "looc"
'''

def main():
    s=input("Enter a string: ")
    reversed_string=""
    for i in range(len(s)):
        reversed_string+=s[-(i+1)]
    print(reversed_string)

if __name__=="__main__":
    main()