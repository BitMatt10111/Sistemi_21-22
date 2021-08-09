'''
Name: Matteo Lamberti
Date: 01/08/21

Output the lyrics to 'The Twelve Days of Christmas'.
'''

from say import say

gifts = ["Drummers Drumming", "Pipers Piping", "Lords-a-Leaping", "Ladies Dancing", "Maids-a-Milking", "Swans-a-Swimming", "Geese-a-Laying", "Gold Rings", "Calling Birds", "French Hens", "Turtle Doves", "Partridge in a Pear Tree"]
days = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth"]

def main():
    second_part = ""
    for i in range(12):
        if i==0:
            output=f"On the {days[i]} day of Christmas my true love gave to me: "
            second_part+=f"{say(i+1,str(i+1))} {gifts[-(i+1)]}"
            output+=second_part
        else:
            output=f"On the {days[i]} day of Christmas my true love gave to me: "
            second_part=f"{say(i+1,str(i+1))} {gifts[-(i+1)]}, {second_part}"
            output+=second_part
        print(output)

if __name__ == "__main__":
    main()