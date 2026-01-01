
class Node:
    def __init__(self, label, value):
        self.__id = label
        self.__value = value

    @property
    def id(self):
        return self.__id
    
    def __hash__(self):
        return self.__id
    def __repr__(self):
        return str(self.__id)

# Simple Graph using adjacency list repr
class Graph:
    def __init__(self):
        self.__nodes = []
        self.__edges = {}

    def addNode(self, node):
        self.__nodes.append(node)

    def addEdge(self, a, b, weight = 0):
        if a not in self.__nodes:
            print(f"{a.__id} node not in graph")
            return False
        if b not in self.__nodes:
            print(f"{b.__id} node not in graph")
            return False
        
        self.__addEdge(a,b, weight)
        self.__addEdge(b,a,weight)
        return True
        
    def __addEdge(self,src,dest,weight):
        if self.__edges.get(src):
            self.__edges.get(src).append((dest,weight))
        else:
            self.__edges[src] = [(dest,weight)]

    def __repr__(self):
        repr = ""
        print(self.__nodes)
        for n in self.__nodes:
            x = [(a[0].id,a[1]) for a in self.__edges.get(n)]
            repr += f"Node {n.id} , AdjList: {x}\n"
        return repr

        

        
