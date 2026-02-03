from Board import Cell
from ClingoSolver import ClingoSolver


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
                print(self.__board.score())
                print(self.__board)
                self.__board.reset()

        return walls

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