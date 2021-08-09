'''
Name: Matteo Lamberti
Date: 01/08/21

Given a phrase, count the occurrences of each word in that phrase.
'''

def main():
    phrase=input("Enter a phrase: ")
    words=phrase.split(" ")
    counter={}
    for word in words:
        if word in counter:
            counter[word]+=1
        else:
            counter[word]=1
    print(counter)

if __name__=="__main__":
    main()
