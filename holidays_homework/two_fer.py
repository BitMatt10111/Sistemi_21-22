'''
Name: Matteo Lamberti
Date: 01/08/21

Given a name, return a string with the message:
One for X, one for me.
Where X is the given name.
'''

def main():
    name=input("Enter a name: ")
    if name == "":
        print("One for you, one for me.")
    else:
        print(f"One for {name}, one for me.")
    
if __name__=="__main__":
    main()