from Board import Cell
from ClingoSolver import ClingoSolver

scoreMap = {
    Cell.CHERRY: 3,
    Cell.BEE: -5,
    Cell.APPLE: 10
}

class Solver(ClingoSolver):
    def __init__(self, board, wallBudget):
        super().__init__(wallBudget)
        self.__board = board
        self.buildSolver()
    
    @property
    def board(self):
        return self.__board

    def solve(self):
        walls = set()
        with super().solve() as hnd:
            for i in hnd:
                print(i)
                for wall in i.symbols(shown=True):
                    x, y = [a.number for a in wall.arguments]
                    walls.add((x,y))
                    self.__board.addWall(x,y)
                print(self.score())
                print(self.__board)
                self.__board.reset()

        return walls

    def score(self):
        def aux(grid, i,j, visited):
            visited[(i,j)] = True
            currentCellScore = 1 + scoreMap.get(grid[i][j]) if scoreMap.get(grid[i][j]) else 1
            neighbours = [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]
            neighbours = [(x,y) for x,y in neighbours if self.__board.inBounds(x,y) and grid[x][y] != Cell.DEAD and grid[x][y] != Cell.WALL]
            # If current cell is portal, the matching portal is also its neighbour
            for _, endpoints in self.__board.portals.items():
                (x,y), (w,z) = endpoints
                if (i,j) == (x,y):
                    neighbours.append((w,z))
                elif (i,j) == (w,z):
                    neighbours.append((x,y))
            for i1,j1 in neighbours:
                if visited.get((i1,j1)):
                    continue
                currentCellScore += aux(grid, i1, j1, visited)

            return currentCellScore
        return aux(self.__board.grid, self.__board.horsePosition[0], self.__board.horsePosition[1], {})
    
    def buildSolver(self):
        for i in range(len(self.__board.grid)):
            for j in range(len(self.__board.grid[0])):
                cell = self.__board.grid[i][j]
                match cell:
                    case Cell.DEAD:
                        super().addWater(i, j)
                    case Cell.HORSE:
                        super().addHorse(i, j)
                    case Cell.CHERRY:
                        super().addCherry(i, j)
                    case Cell.APPLE:
                        super().addApple(i, j)
                    case Cell.BEE:
                        super().addBee(i, j)
                if(self.__board.isBoundary(i,j)):
                    super().addBoundary(i,j)
                super().addNode(i,j)

        for _, endpoints in self.__board.portals.items():
            (i,j), (i2,j2) = endpoints
            super().addPortal(i,j,i2,j2)