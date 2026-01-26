from math import inf
IN_NODE = 0
OUT_NODE = 1
SINK_NODE = 2
WALL_COST = 1
# Separate node type because i still dont understand the algorithm fully
class NetworkNode:
    def __init__(self, type, id):
        self.type = type
        self.id = id
    
    def __hash__(self):
        return hash((self.id, self.type))
    
    def __eq__(self, other):
        return self.id == other.id and self.type == other.type
    
    
    def __repr__(self):
        return str((self.id, "VIN" if self.type == 0 else "VOUT" if self.type == 1 else "SINK"))

class FlowNetwork:
    def __init__(self):
        self.vertexes = set()
        self.edges = {}

    def addVertex(self, nodeId):
        vin = NetworkNode(IN_NODE,nodeId)
        vout = NetworkNode(OUT_NODE,nodeId)
        self.vertexes.add(vin)
        self.vertexes.add(vout)
        if not self.edges.get(vin):
            self.edges[vin] = [(vout, WALL_COST)]
        else:
            self.edges[vin].append((vout, WALL_COST))
    
    def addSink(self, nodeId):
        vin = NetworkNode(SINK_NODE,nodeId)
        self.vertexes.add(vin)

    def addEdge(self, srcId, destId):
        if NetworkNode(SINK_NODE, srcId) in self.vertexes:
            return
        self.__addEdge(srcId, destId)
        self.__addEdge(destId, srcId)

    def addEdgeToSink(self, srcId, destId):
        if NetworkNode(SINK_NODE, srcId) in self.vertexes:
            return
        self.__addEdge(srcId, destId, True)

    def __addEdge(self, srcId, destId, toSink = False):
        v = NetworkNode(OUT_NODE, srcId)
        u = NetworkNode(IN_NODE if not toSink else SINK_NODE, destId)
        if v not in self.vertexes:
            return
        if u not in self.vertexes:
            return
        if not self.edges.get(v):
            self.edges[v] = [(u, inf)]
        else:
            edges = self.edges[v]
            if (u, inf) not in edges:
                self.edges[v].append((u, inf))
        

    def __repr__(self):
        repr = ""
        repr += str(self.vertexes) + "\n"
        for i,j in self.edges.items():
            repr += f"{i}, AdjList: {j}\n"
        return repr
        
