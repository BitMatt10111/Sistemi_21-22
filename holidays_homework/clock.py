'''
Name: Matteo Lamberti
Date: 01/08/21

Implement a clock that handles times without dates.
You should be able to add and subtract minutes to it.
Two clocks that represent the same time should be equal to each other.
'''

import math

class clock():
    def __init__(self,h,m):
        self.hours=h%24
        if m<60:
            self.minutes=m
        else:
            self.minutes=0
            self.add(m)
    def add(self,m):
        self.minutes+=m
        h=int(self.minutes/60)
        self.hours+=h
        self.hours=self.hours%24
        self.minutes=self.minutes-(60*h)
    def sub(self,m):
        h=math.ceil(m/60)
        h=h%24
        self.minutes-=(m-60*h)
        self.hours-=h

def main():
    clk=clock(37,60)
    clk.sub(125)
    clk.add(42)
    print(clk.hours)
    print(clk.minutes)

if __name__=="__main__":
    main()