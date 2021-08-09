'''
Name: Matteo Lamberti
Date: 30/7/21

Given a list of values for five dice and a category,
your solution should return the score of the dice for
that category. If the dice do not satisfy the
requirements of the category your solution should return 0.

Categories: https://en.wikipedia.org/wiki/Yacht_(dice_game)

'''

def ones(dl):
    print(f"Score: {dl.count(1)*1}")

def twos(dl):
    print(f"Score: {dl.count(2)*2}")

def threes(dl):
    print(f"Score: {dl.count(3)*3}")

def fours(dl):
    print(f"Score: {dl.count(4)*4}")

def fives(dl):
    print(f"Score: {dl.count(5)*5}")

def sixes(dl):
    print(f"Score: {dl.count(6)*6}")

def full_house(dl):
    value1=dl[0]
    for dice in dl[1:]:
        if dice!=value1:
            value2=dice
    if dl.count(value1)==3 and dl.count(value2)==2 or dl.count(value1)==2 and dl.count(value2)==3:
        print(f"Score: {sum(dl)}")
    else:
        print("Score: 0")

def four_of_a_kind(dl):
    value1=dl[0]
    for dice in dl[1:]:
        if dice!=value1:
            value2=dice
    if dl.count(value1)==4:
        print(f"Score: {value1*4}")
    elif dl.count(value2)==4:
        print(f"Score: {value2*4}")
    else:
        print("Score: 0")

def little_straight(dl):
    if 1 in dl and 2 in dl and 3 in dl and 4 in dl and 5 in dl:
        print("Score: 30")
    else:
        print("Score: 0")

def big_straight(dl):
    if 6 in dl and 2 in dl and 3 in dl and 4 in dl and 5 in dl:
        print("Score: 30")
    else:
        print("Score: 0")

def choice(dl):
    print(f"Score: {sum(dl)}")

def yacht(dl):
    yacht=True
    value=dl[0]
    for dice in dl[1:]:
        if dice!=value:
            yacht=False
            break
    if yacht==True:
        print("Score: 50")
    else:
        print("Score: 0")

def main():
    dice_list=[int(input("Enter the first dice: ")),int(input("Enter the second dice: ")),int(input("Enter the third dice: ")),int(input("Enter the fourth dice: ")),int(input("Enter the fifth dice: "))]
    cat=input("Enter a category (write one of this: ones, twos, threes, fours, fives, sixes, full_house, four_of_a_kind, little_straight, big_straight, choice, yacht): ")
    eval(cat + "(dice_list)")

if "__main__"==__name__:
    main()

