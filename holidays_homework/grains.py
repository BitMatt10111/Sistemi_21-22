'''
Author: Matteo Lamberti
Date: 02/08/21

Calculate the number of grains of
wheat on a chessboard given that the number on each square doubles.
'''

squares=64

def main():
    cell=int(input("Enter a cell: "))
    grains=[1]
    for i in range(1,64):
        grains.append(grains[i-1]*2)
    print(grains[cell-1])
    print(sum(grains))

if __name__=="__main__":
    main()