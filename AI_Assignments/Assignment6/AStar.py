import math
import heapq
import networkx as nx
import matplotlib.pyplot as plt

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

def drawGraph(graph, path, save_path=None):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor, cost in neighbors[0]:
            G.add_edge(node, neighbor, weight=cost)

    pos = {node: graph[node][1] for node in graph}
    labels = {(node, neighbor): cost for node, neighbors in graph.items() for neighbor, cost in neighbors[0]}

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    if save_path:
        plt.savefig(save_path, format="PNG")  # Save the figure as a PNG image
    else:
        plt.show()

# Graph representation as a dictionary
graph = {
    'S': [[('A', 3), ('B', 2)], (0, 0)],
    'A': [[('C', 4), ('D', 1)], (7, 6)],
    'B': [[('E', 3), ('F', 1)], (1, 3)],
    'E': [[('H', 5)], (6, 2)],
    'F': [[('I', 2), ('G', 3)], (1, 1)],
    'C': [[], (4, 3)],  # Empty neighbor list
    'D': [[], (1, 2)],  # Empty neighbor list
    'H': [[], (2, 2)],  # Empty neighbor list
    'I': [[], (5, 4)],  # Empty neighbor list
    'G': [[], (-1, 1)]  # Empty neighbor list
}

def main():
    startNode = 'S'
    goalNode = 'G'
    heuristicType = "manhattan"  # Change to "euclidean" for Euclidean heuristic

    print("Start Node:", startNode)
    print("Goal Node:", goalNode)
    print("Heuristic:", heuristicType.capitalize())

    # Instantiate AStar with the correct arguments
    astarAlgorithm = AStar(graph, startNode, goalNode, heuristicType)
    path = astarAlgorithm.astar()

    print("Path Found:")
    printPath(path)

    # Draw and save the graph
    drawGraph(graph, path, save_path="AI_Assignments/Assignment6/graphAStar.png")  # Specify the save_path to save the image

if __name__ == "__main__":
    main()