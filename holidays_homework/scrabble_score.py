'''
Author: Matteo Lamberti
Date: 02/08/21

Given a word, compute the scrabble score for that word.
'''

score_dict={1:['a','e','i','o','u','l','n','r','s','t'],2:['d','g'],3:['b','c','m','p'],4:['f','h','v','w','y'],5:['k'],8:['j','x'],10:['q','z']}

def main():
    word=input("Enter a word: ")
    score=0
    for letter in word:
        if letter in score_dict[1]:
            score+=1
        elif letter in score_dict[2]:
            score+=2
        elif letter in score_dict[3]:
            score+=3
        elif letter in score_dict[4]:
            score+=4
        elif letter in score_dict[5]:
            score+=5
        elif letter in score_dict[8]:
            score+=8
        elif letter in score_dict[10]:
            score+=10
    print(f"Your score is: {score}")
        

if __name__=="__main__":
    main()