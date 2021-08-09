'''
Author: Matteo Lamberti
Date: 02/08/21

Given a string containing brackets [], braces {},
parentheses (), or any combination thereof,
verify that any and all pairs are
matched and nested correctly.
'''

def main():
    string=input("Enter some nested brackets: ")
    if len(string)%2==0:
        opening_brackets=['(','[','{']
        ending_brackets=[')',']','}']
        ob=[]
        eb=[]
        for b in string:
            if b in opening_brackets:
                ob.append(b)
            if b in ending_brackets:
                eb.append(b)
        matching=True
        for i in range(len(ob)):
            if ord(ob[i])!=ord(eb[-(i+1)])-1 and ord(ob[i])!=ord(eb[-(i+1)])-2:
                matching=False
        if matching==True:
            print("The brackets are correctly nested")
        else:
            print("The brackets are not correctly nested")
    else:
        print("The brackets are not correctly nested")

if __name__=="__main__":
    main()