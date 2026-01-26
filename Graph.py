
class Node:
    def __init__(self, label, isBoundaryNode = False):
        self.__id = label
        self.__isBoundaryNode = isBoundaryNode
        self.__blocked = False

    @property
    def blocked(self):
        return self.__blocked
    
    @blocked.setter
    def blocked(self, value):
        self.__blocked = value

    @property
    def id(self):
        return self.__id
    
    @property
    def isBoundaryNode(self):
        return self.__isBoundaryNode
    
    def __hash__(self):
        return hash(self.__id)
    def __repr__(self):
        return str(f"({self.id}, {self.isBoundaryNode}, {self.__blocked})")

# Simple Graph using adjacency list repr
class Graph:
    def __init__(self):
        self.__nodes = {}
        self.__edges = {}

    @property
    def nodes(self):
        return self.__nodes
    
    @property
    def edges(self):
        return self.__edges
    
    def addNode(self, node):
        self.__nodes[node.id] = node

    def addEdge(self, a, b, weight = 1):
        if a.id not in self.__nodes.keys():
            print(f"{a.__id} node not in graph")
            return False
        if b.id not in self.__nodes.keys():
            print(f"{b.__id} node not in graph")
            return False
        
        self.__addEdge(a,b, weight)
        self.__addEdge(b,a,weight)
        return True
        
    def __addEdge(self,src,dest,weight):
        if self.__edges.get(src):
            if dest.id in [a.id for a,b in self.__edges.get(src)]:
                return
            self.__edges.get(src).append((dest,weight))
        else:
            self.__edges[src] = [(dest,weight)]

    def __repr__(self):
        repr = ""
        print(self.__nodes)
        for n in self.__nodes.values():
            x = [(a[0].id,a[1]) for a in self.__edges.get(n,[])]
            repr += f"Node {n.id} , AdjList: {x}\n"
        return repr

    def reachable(self, src, dest, visited:set):
        if src.id in visited:
            return False
        if dest in [a for a,_ in self.__edges.get(src,[])]:
            return True
        visited.add(src.id)
        return any([self.reachable(a[0], dest, visited) for a in self.__edges.get(src) if not a[0].blocked])

        

        
