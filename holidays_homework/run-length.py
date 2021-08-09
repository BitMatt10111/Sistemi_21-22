'''
Author: Matteo Lamberti
Date: 02/08/21

Implement run-length encoding and decoding.
'''

def main():
    string=input("Enter a string to be encoded: ")
    string+=" "
    final_string=""
    i=1
    current_letter=string[0]
    for letter in string[1:]:
        if letter == current_letter:
            i+=1
        else:
            if i==1:
                final_string+=f"{current_letter}"
            else:
                final_string+=f"{i}{current_letter}"
            current_letter=letter
            i=1
    print(f"Encoded: {final_string}")

if __name__=="__main__":
    main()