from Board import *
from Graph import *


def main():
    board = Board("~~S~~.~~~.~\n~~....~~~..\n...~~.~S~.~\n~~~~S......\n~~S~~.~C~.~\n.....H.....\n~~~.~.~~.~~\n~SS.~.S~...\n~S~.~.~~S~.\n~.~......~~\n....~.~....\n~~~.~.~.~~~")
    print(board)

    while True:
        print(board)
        i, j = [int(a) for a in input().split()]
        board.addWall(i,j)
        print(board.enclosed())


if __name__ == "__main__":
    main()