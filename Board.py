class Board:
    def __init__(self, str: str):
        self.__mapStr = str
        self.__grid = self.__parseMapStr()


    def addWall(self,i,j):
        if not self.__inBounds(i,j):
            return False
        if self.__grid[i][j] != "🟩":
            return False
        self.__grid[i][j] = "⬜"
        return True
    
    def removeWall(self,i,j):
        if not self.__inBounds(i,j):
            return False
        if self.__grid[i][j] != "⬜":
            return False
        self.__grid[i][j] = "🟩"
        return True

    def __toCell(self,char: str):
        match char:
            case '~':
                return "💧"
            case '.':
                return "🟩"
            case 'C':
                return "C"
            case 'S':
                return "🐝"
            case 'H':
                return "🐴"
            case 'G':
                return "G"
            # White square for box placement: ⬜
        return char

    def __inBounds(self,i,j):
        return 0 <= i < len(self.__grid) and 0 <= j < len(self.__grid[0])
    
    def __toPrettyCell(self, char: str):
        match char:
            case '~':
                return "💧"
            case '.':
                return "🟩"
            case 'C':
                return "C"
            case 'S':
                return "🐝"
            case 'H':
                return "🐴"
            case 'G':
                return "G"
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
                if grid[i][j] == "🐴":
                    self.horse = (i,j)
        return grid


    def __repr__(self):
        repr = "─"*len(self.__grid[0])*2 + "\n"
        for row in self.__grid:
            repr += "│" + "".join([self.__toPrettyCell(c) for c in row]) + "│\n"
        repr += "─"*len(self.__grid[0])*2 + "\n"
        return repr