'''
Name: Matteo Lamberti
Date: 01/08/21

Write a function to convert from normal numbers to Roman Numerals.
'''
    #print("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n")

    #print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")

start=99

def main():
    for i in range(start,-1,-1):
        if i==1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n")
        elif i==0:
            print(f"no more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {start} bottles of beer on the wall.\n")
        else: 
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i-1} bottles of beer on the wall.\n")

        
if __name__ == "__main__":
    main()