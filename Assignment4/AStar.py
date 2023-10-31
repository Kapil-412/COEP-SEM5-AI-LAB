import math
import heapq

class AStar:
    def __init__(self, graph, start, goal, heuristic):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.heuristic = heuristic
        self.openList = []
        self.closedList = set()
        self.g = {node: float('inf') for node in graph}
        self.g[start] = 0
        self.parents = {node: None for node in graph}

    def heuristicCost(self, node):
        x1, y1 = self.graph[node][1]
        x2, y2 = self.graph[self.goal][1]
        if self.heuristic == "manhattan":
            return abs(x2 - x1) + abs(y2 - y1)
        elif self.heuristic == "euclidean":
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def astar(self):
        heapq.heappush(self.openList, (self.g[self.start] + self.heuristicCost(self.start), self.start))

        while self.openList:
            _, currentNode = heapq.heappop(self.openList)

            if currentNode == self.goal:
                path = []
                while self.parents[currentNode] is not None:
                    path.append(currentNode)
                    currentNode = self.parents[currentNode]
                path.append(self.start)
                path.reverse()
                return path

            self.closedList.add(currentNode)

            for neighbor, cost in self.graph[currentNode][0]:
                tentativeG = self.g[currentNode] + cost
                if tentativeG < self.g[neighbor]:
                    self.parents[neighbor] = currentNode
                    self.g[neighbor] = tentativeG
                    heapq.heappush(self.openList, (tentativeG + self.heuristicCost(neighbor), neighbor))

        return []

def printPath(path):
    if not path:
        print("No path found.")
    else:
        print("Path:", " -> ".join(path))

# Graph representation as a dictionary
graph = {
    'S': [[('A', 3), ('B', 2)], (0, 0)],
    'A': [[('C', 4), ('D', 1)], (7, 6)],
    'B': [[('E', 3), ('F', 1)], (1, 3)],
    'E': [[('H', 5)], (6, 2)],
    'F': [[('I', 2), ('G', 3)], (1, 1)],
    'C': [[()], (4, 3)],
    'D': [[()], (1, 2)],
    'H': [[()], (2, 2)],
    'I': [[()], (5, 4)],
    'G': [[()], (-1, 1)]
}

def main():
    startNode = 'S'
    goalNode = 'G'
    heuristicType = "manhattan"  # Change to "euclidean" for Euclidean heuristic

    print("Start Node:", startNode)
    print("Goal Node:", goalNode)
    print("Heuristic:", heuristicType.capitalize())

    astarAlgorithm = AStar(graph, startNode, goalNode, heuristicType)
    path = astarAlgorithm.astar()

    print("Path Found:")
    printPath(path)

if __name__ == "__main__":
    main()