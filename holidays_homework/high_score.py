'''
Author: Matteo Lamberti
Date: 23/07/21

Your task is to build a high-score component
of the classic Frogger game, one of the highest
selling and addictive games of all time,
and a classic of the arcade era. Your task
is to write methods that return the highest
score from the list, the last added score
and the three highest scores.
'''

def top3(l):
    top3=[]
    val1=l[0]
    val2=l[1]
    val3=l[2]
    for val in l[3:]:
        if val>val1:
            if val3<val2:
                val3=val2
            if val2<val1:
                val2=val1
            val1=val
        elif val>val2:
            if val3<val2:
                val3=val2
            val2=val
        elif val> val3:
            val3=val
    return val1,val2,val3

def highest(l):
    return max(l)

def last(l):
    return l[-1]

def main():
    hs_list=[23,100,123,200,223,300]
    print(f"Top 3: {top3(hs_list)}")
    print(f"Highest: {highest(hs_list)}")
    print(f"Last added: {last(hs_list)}")

if __name__=="__main__":
    main()