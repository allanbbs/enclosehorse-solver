import clingo


class ClingoContext:
    def node(self, i, j):
        return (i,j)


class ClingoSolver:
    def __init__(self, k):
        self.solver = clingo.Control()
        self.wallBudget = k

    def addNode(self, i, j):
        self.solver.add("base", [],
        f"""\
            node({i},{j}).
        """)

    def addHorse(self, i, j):
        self.solver.add("base", [],
        f"""\
            horse({i},{j}).
        """)

    def addBoundary(self, i, j):
        self.solver.add("base", [],
        f"""\
            boundary({i},{j}).
        """)

    def addBee(self, i, j):
        self.solver.add("base", [],
        f"""\
            bee({i},{j}).
        """)

    def addCherry(self, i, j):
        self.solver.add("base", [],
        f"""\
            cherry({i},{j}).
        """)

    def addApple(self, i, j):
        self.solver.add("base", [],
        f"""\
            apple({i},{j}).
        """)

    def addWater(self, i, j):
        self.solver.add("base", [],
        f"""\
            water({i},{j}).
        """)

    def __addBaseRules(self):
        command = f"""\
            #const walls={self.wallBudget}.
            adj(I, J, I+1, J) :- node(I,J), node(I+1, J).
            adj(I, J, I, J+1) :- node(I,J), node(I, J+1). 
            adj(I, J, I-1, J) :- node(I,J), node(I-1, J). 
            adj(I, J, I, J-1) :- node(I,J), node(I, J-1). 

            valid(I, J) :- node(I,J), not water(I,J).

            {{wall(I, J)}} :- valid(I,J), not apple(I,J), not cherry(I,J), not bee(I,J).

            :- #count {{ I,J : wall(I,J) }} > walls.
  
            z(I,J) :- horse(I,J).
            z(R2,C2) :- z(R1,C1), adj(R1,C1, R2,C2), valid(R2,C2), not wall(R2, C2).
            
            :- z(I,J), boundary(I,J).
            
            #maximize {{ 4,I,J : z(I,J), cherry(I,J) ; 11,I,J : z(I,J), apple(I,J) ; -4,I,J : z(I,J), bee(I,J) ; 1,I,J : z(I,J), not cherry(I,J), not apple(I,J), not bee(I,J) }}.
            
            #show wall/2.
        """
        self.solver.add("base", [], command)

    def solve(self):
        self.__addBaseRules()
        self.solver.ground([("base", [])], context=ClingoContext())
        return self.solver.solve(yield_=True)
