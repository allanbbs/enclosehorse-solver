from Graph import Graph, Node


class Board:
    def __init__(self, str: str):
        self.__mapStr = str
        self.__center = (0,0)
        self.__grid = self.__parseMapStr()
        self.__graph = self.__toGraph()


    @property
    def graph(self):
        return self.__graph
    
    def addWall(self,i,j):
        if not self.__inBounds(i,j):
            return False
        if self.__grid[i][j] != ".":
            return False
        self.__grid[i][j] = "x"
        self.__graph.nodes.get((i,j)).blocked = True
        return True
    
    def removeWall(self,i,j):
        if not self.__inBounds(i,j):
            return False
        if self.__grid[i][j] != "x":
            return False
        self.__grid[i][j] = "."
        self.__graph.nodes.get((i,j)).blocked = False
        return True

    def __toCell(self,char: str):
        return char

    def __inBounds(self,i,j):
        return 0 <= i < len(self.__grid) and 0 <= j < len(self.__grid[0])
    
    def __getNeihbours(self, i, j):
        candidates = [(i+1,j), (i-1, j), (i, j+1), (i, j-1)]
        return [(i,j) for i,j in candidates if self.__inBounds(i,j) and self.__grid[i][j] != '~']

    def __toGraph(self):
        graph = Graph()
        sinkNode = Node((-1,-1), True, 1000)
        graph.addNode(sinkNode)
        rows = len(self.__grid)
        cols = len(self.__grid[0])
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[0])):
                if self.__grid[i][j] == "~":
                   continue
                isBoundaryNode = self.__grid[i][j] != "~" and (i == 0 or j == 0 or i ==(rows-1) or j == (cols-1) )
                n = Node((i,j),isBoundaryNode,1)
                graph.addNode(n)
                # Connect boundary nodes to sink
                if isBoundaryNode:
                    graph.addEdge(n, sinkNode)
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[0])):
                for adjI, adjJ in self.__getNeihbours(i,j):
                    if self.__grid[i][j] == "~":
                        continue
                    src = graph.nodes.get((i,j))
                    if not src:
                        continue
                    dest = graph.nodes.get((adjI,adjJ))
                    graph.addEdge(src, dest)
        print(graph)
        return graph

    
    def __toPrettyCell(self, char: str):
        match char:
            case '~':
                return "💧"
            case '.':
                return "🟩"
            case 'x':
                return "⬜"
            case 'C':
                return "🍇"
            case 'S':
                return "🐝"
            case 'H':
                return "🐴"
            case 'G':
                return "🍎"
            # White square for box placement: ⬜
        return char
            
    def __parseMapStr(self):
        lines = self.__mapStr.split("\n")
        rows = len(lines)
        cols = len(lines[0])
        print(f"{rows}x{cols}")
        grid = [[None] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = self.__toCell(lines[i][j])
                if grid[i][j] == "H":
                    self.__center = (i,j)
        return grid
    
    def enclosed(self):
        sinkNode = self.__graph.nodes.get((-1,-1))
        mainNode = self.__graph.nodes.get(self.__center)
        return not self.__graph.reachable(mainNode,sinkNode, set())


    def __repr__(self):
        repr = "─"*len(self.__grid[0])*2 + "\n"
        for row in self.__grid:
            repr += "│" + "".join([self.__toPrettyCell(c) for c in row]) + "│\n"
        repr += "─"*len(self.__grid[0])*2 + "\n"
        return repr