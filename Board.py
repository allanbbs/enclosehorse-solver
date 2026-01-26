from Graph import Graph, Node


class Board:
    def __init__(self, str: str):
        self.__mapStr = str
        self.__horse = (0,0)
        self.__grid = self.__parseMapStr()
        
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
        if self.__grid[i][j] != ".":
            return False
        self.__grid[i][j] = "x"
        return True
    
    def removeWall(self,i,j):
        if not self.inBounds(i,j):
            return False
        if self.__grid[i][j] != "x":
            return False
        self.__grid[i][j] = "."
        return True
    
    def inBounds(self,i,j):
        return 0 <= i < len(self.__grid) and 0 <= j < len(self.__grid[0])

    def __toCell(self,char: str):
        return char

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
                return "💀" # -> Yeti easter egg xd
            case 'G':
                return "🍎"
        if char.isdigit():
            raise("Portals are not supported yet")

        return char
            
    def __parseMapStr(self):
        lines = self.__mapStr.split("\n")
        rows = len(lines)
        cols = len(lines[0])
        print(self.__mapStr)
        print(f"{rows}x{cols}")
        grid = [[None] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = self.__toCell(lines[i][j])
                if grid[i][j] == "H":
                    self.__horse = (i,j)
        return grid

    def __repr__(self):
        repr = "─"*len(self.__grid[0])*2 + "\n"
        for row in self.__grid:
            repr += "│" + "".join([self.__toPrettyCell(c) for c in row]) + "│\n"
        repr += "─"*len(self.__grid[0])*2 + "\n"
        return repr