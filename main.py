from Board import *


def main():
    board = Board("...~~~~~.S.~.\n~............\n~~..~~~~~..~.\n~~~.~SSS~.~~.\n~...~SSS~.~~~\n~S..~~.~~..~~\n.............\n.~~..H...~~.S\n~~~....~~~~.~\n~...~~.~~....\n.S.~~~....~~.\n....~~...~~~.\n~..~~~....~~.\n~~~~......S..\n~S~..S.~~~~~~")
    print(board)
    while True:
        i,j = [int(a) for a in input().split()]
        board.addWall(i,j)
        print(board)



if __name__ == "__main__":
    main()