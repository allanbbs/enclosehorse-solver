from Board import *
from Graph import *
from Solver import Solver


def main():
    board = Board("~~S~~.~~~.~\n~~....~~~..\n...~~.~S~.~\n~~~~S......\n~~S~~.~C~.~\n.....H.....\n~~~.~.~~.~~\n~SS.~.S~...\n~S~.~.~~S~.\n~.~......~~\n....~.~....\n~~~.~.~.~~~")
    solver = Solver(board)
    while True:
        print(board)
        i, j = [int(a) for a in input().split()]
        solver.addWall(i,j)
        print(solver.enclosed())


if __name__ == "__main__":
    main()