from enum import Enum

class Cell(Enum):
    DEAD = 0
    HORSE = 1
    CHERRY = 2
    APPLE = 3
    BEE = 4
    GRASS = 5
    WALL = 6
    MARKED = -1

scoreMap = {
    Cell.CHERRY: 3,
    Cell.BEE: -5,
    Cell.APPLE: 10
}

class Board:
    def __init__(self, str: str):
        self.__mapStr = str
        self.__horse = (0,0)
        self.__grid = None
        self.__parseMapStr()
        self.marked = {}
        
    @property
    def grid(self):
        return self.__grid
    
    @property
    def horsePosition(self):
        return self.__horse
    
    @property
    def dimensions(self):
        return len(self.__grid), len(self.__grid[0])
    
    def addWall(self,i,j):
        if not self.inBounds(i,j):
            return False
        if self.__grid[i][j] != Cell.GRASS:
            return False
        self.__grid[i][j] = Cell.WALL
        return True

    def inBounds(self,i,j):
        return 0 <= i < len(self.__grid) and 0 <= j < len(self.__grid[0])

    def isBoundary(self, i, j):
        isTopDownEdge = i==0 or (i == len(self.__grid) - 1)
        isLeftRightEdge = j==0 or (j == len(self.__grid[0]) - 1)
        return self.__grid[i][j] and (isTopDownEdge or isLeftRightEdge)
    
    def reset(self):
        self.__parseMapStr()
        self.marked ={}

    def score(self):
        def aux(grid, i,j, visited):
            visited[(i,j)] = True
            self.marked[(i,j)] = True
            currentCellScore = 1 + scoreMap.get(grid[i][j]) if scoreMap.get(grid[i][j]) else 1
            neighbours = [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]
            neighbours = [(x,y) for x,y in neighbours if self.inBounds(x,y) and grid[x][y] != Cell.DEAD and grid[x][y] != Cell.WALL]
            for i1,j1 in neighbours:
                if visited.get((i1,j1)):
                    continue
                currentCellScore += aux(grid, i1, j1, visited)

            return currentCellScore
        return aux(self.__grid, self.horsePosition[0], self.horsePosition[1], {})

    def __toCell(self,char: str):
        match char:
            case '~':
                return Cell.DEAD
            case '.':
                return Cell.GRASS
            case 'x':
                return Cell.WALL
            case 'C':
                return Cell.CHERRY
            case 'S':
                return Cell.BEE
            case 'H':
                return Cell.HORSE # -> Yeti easter egg xd
            case 'G':
                return Cell.APPLE
        if char.isdigit():
            raise("Portals are not supported yet")

    def __toPrettyCell(self, char):
        self.k = 0
        match char:
            case Cell.GRASS:
                return "🟩"
            case Cell.WALL:
                return "⬜"
            case Cell.CHERRY:
                return "🍇"
            case Cell.BEE:
                return "🐝"
            case Cell.HORSE:
                return "💀" # -> Yeti easter egg xd
            case Cell.APPLE:
                return "🍎"
            case Cell.DEAD:
                return "💧"
        raise(Exception("Portals are not supported yet"))
            
    def __parseMapStr(self):
        lines = self.__mapStr.split("\n")
        rows = len(lines)
        cols = len(lines[0])
        grid = [[None] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = self.__toCell(lines[i][j])
                if grid[i][j] == Cell.HORSE:
                    self.__horse = (i,j)
        self.__grid = grid

    def __repr__(self):
        repr = "─"*len(self.__grid[0])*2 + "\n"
        for row in self.__grid:
            repr += "│" + "".join([self.__toPrettyCell(c) for c in row]) + "│\n"
        repr += "─"*len(self.__grid[0])*2 + "\n"
        return repr
