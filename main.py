from Board import *
from Graph import *


def main():
    board = Board("...~~~~~.S.~.\n~............\n~~..~~~~~..~.\n~~~.~SSS~.~~.\n~...~SSS~.~~~\n~S..~~.~~..~~\n.............\n.~~..H...~~.S\n~~~....~~~~.~\n~...~~.~~....\n.S.~~~....~~.\n....~~...~~~.\n~..~~~....~~.\n~~~~......S..\n~S~..S.~~~~~~")
    print(board)
    graph = Graph()
    a0 = Node(0,None)
    a1 = Node(1,None)
    a2 = Node(2,None)
    a3 = Node(3,None)
    a4 = Node(4,None)


    graph.addNode(a1)
    graph.addNode(a2)
    graph.addNode(a3)
    graph.addNode(a4)
    graph.addNode(a0)
    graph.addEdge(a2,a1)
    graph.addEdge(a2,a0)
    graph.addEdge(a2,a3)
    graph.addEdge(a3,a4)
    print(graph)
    while True:
        i,j = [int(a) for a in input().split()]
        board.addWall(i,j)
        print(board)



if __name__ == "__main__":
    main()