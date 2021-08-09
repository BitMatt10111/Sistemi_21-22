'''
Author: Matteo Lamberti
Date: 02/08/21

Calculate the Hamming Distance between two DNA strands.
'''

def main():
    while True:
        strand1=input("Enter the first strand: ")
        strand2=input("Enter the second strand: ")
        if len(strand1)==len(strand2):
            break
    highlighter=""
    for i in range(len(strand1)):
        if strand1[i]!=strand2[i]:
            highlighter+='^'
        else:
            highlighter+=' '
    print(strand1)
    print(strand2)
    print(highlighter)

if __name__=="__main__":
    main()
        