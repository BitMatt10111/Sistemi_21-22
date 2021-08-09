'''
Name: Matteo Lamberti
Date: 31/7/21

An anagram is a rearrangement of letters
to form a new word. Given a word and a
list of candidates, select the sublist
of anagrams of the given word.
Given "listen" and a list of candidates
like "enlists" "google" "inlets" "banana" 
the program should return a list
containing "inlets".
'''

def main():
    word=input("Enter a word: ")
    candidates=[]
    while True:
        candidate=input("Enter a candidate: ")
        candidates.append(candidate)
        ans=input("It's enough (write 'yes' to stop)? ")
        if ans=="yes" or ans=="YES":
            break
    for candidate in candidates:
        is_anagram=True
        for letter in candidate:
            if not letter in word:
                is_anagram=False
        if is_anagram==True:
            anagram=candidate
    print(f"The anagram is: {anagram}")

if "__main__"==__name__:
    main()