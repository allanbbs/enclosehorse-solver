from enum import Enum

class Cell(Enum):
    DEAD = 0
    HORSE = 1
    CHERRY = 2
    APPLE = 3
    BEE = 4
    GRASS = 5
    WALL = 6

class Board:
    def __init__(self, str: str):
        self.__mapStr = str
        self.__horse = (0,0)
        self.__grid = None
        self.__portals = {}
        self.__parseMapStr()
        
    @property
    def portals(self):
        return self.__portals

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
        self.portals.clear()
        self.__parseMapStr()
        self.marked ={}

    def __toCell(self,char: str, i, j):
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
            portalId = int(char)
            print(f"Adding portal with id {portalId}")
            if not self.__portals.get(portalId):
                self.__portals[portalId] = [(i,j)]
            else:
                self.__portals.get(portalId).append((i,j))
            return portalId

        raise Exception(f"Unsupported char {char}")

    def __toPrettyCell(self, char):
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
        return "🚪"
            
    def __parseMapStr(self):
        lines = self.__mapStr.split("\n")
        rows = len(lines)
        cols = len(lines[0])
        grid = [[None] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = self.__toCell(lines[i][j], i, j)
                if grid[i][j] == Cell.HORSE:
                    self.__horse = (i,j)
        self.__grid = grid

    def __repr__(self):
        repr = "─"*len(self.__grid[0])*2 + "\n"
        for row in self.__grid:
            repr += "│" + "".join([self.__toPrettyCell(c) for c in row]) + "│\n"
        repr += "─"*len(self.__grid[0])*2 + "\n"
        return repr
