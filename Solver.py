from Board import Board
from FlowNetwork import FlowNetwork
from Graph import Graph, Node


class Solver:
    def __init__(self, board):
        self.__board = board
        self.__graph = self.__toGraph(board)
        f = FlowNetwork()
        for i,j in self.__graph.nodes.items():
            if i == (-1,-1):
                f.addSink(i)
                continue
            f.addVertex(i)
        for i,j in self.__graph.nodes.items():
            edges = self.__graph.edges.get(j)
            if j.isBoundaryNode:
                f.addEdgeToSink(i, (-1,-1))
            for edge,w in edges:
                f.addEdge(i, edge.id)
        print(f)

    def enclosed(self):
        sinkNode = self.__graph.nodes.get((-1,-1))
        mainNode = self.__graph.nodes.get(self.__board.horsePosition)
        return not self.__graph.reachable(mainNode,sinkNode, set())
    
    def addWall(self, i, j):
        if self.__board.addWall(i, j):
            self.__graph.nodes.get((i,j)).blocked = True

    
    def __getNeihbours(self, i, j):
        candidates = [(i+1,j), (i-1, j), (i, j+1), (i, j-1)]
        return [(i,j) for i,j in candidates if self.__board.inBounds(i,j) and self.__board.grid[i][j] != '~']
    
    def __toGraph(self, board: Board):
        graph = Graph()
        sinkNode = Node((-1,-1), True)
        graph.addNode(sinkNode)
        rows, cols = board.dimensions
        for i in range(rows):
            for j in range(cols):
                if self.__board.grid[i][j] == "~":
                   continue
                isBoundaryNode = self.__board.grid[i][j] != "~" and (i == 0 or j == 0 or i ==(rows-1) or j == (cols-1) )
                n = Node((i,j),isBoundaryNode)
                graph.addNode(n)
                # Connect boundary nodes to sink
                if isBoundaryNode:
                    graph.addEdge(n, sinkNode)
        for i in range(rows):
            for j in range(cols):
                for adjI, adjJ in self.__getNeihbours(i,j):
                    if self.__board.grid[i][j] == "~":
                        continue
                    src = graph.nodes.get((i,j))
                    if not src:
                        continue
                    dest = graph.nodes.get((adjI,adjJ))
                    graph.addEdge(src, dest)
        print(graph)
        return graph