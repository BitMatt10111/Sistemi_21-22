'''
Name: Matteo Lamberti
Date: 01/08/21

Correctly determine the fewest number of
coins to be given to a customer such that
the sum of the coins' value would
equal the correct amount of change.
'''

def main():
    change=int(input("Enter the change amount: "))
    coins_set=[]
    while True:
        coin=int(input("Enter a coin value: "))
        coins_set.append(coin)
        ans=input("It's enough (write 'yes' to stop)? ")
        if ans=="yes" or ans=="YES":
            break
    change_coins=[]
    last_coin=0
    while change!=0:
        for coin in coins_set[1:]:
            if int(change/coin)<1:
                break
            last_coin=coin
        if last_coin==0:
            last_coin=coins_set[0]
        change_coins.append(last_coin)
        change-=last_coin
    print(change_coins)

if "__main__"==__name__:
    main()