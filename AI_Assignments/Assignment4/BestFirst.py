import math
import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'S': [['A', 'B'], (0, 0)],
    'A': [['C', 'D'], (7, 6)],
    'B': [['E', 'F'], (1, 3)],
    'E': [['H'], (6, 2)],
    'F': [['I', 'G'], (1, 1)],
    'C': [[] , (4, 3)],
    'D': [[] , (1, 2)],
    'H': [[] , (2, 2)],
    'I': [[] , (5, 4)],
    'G': [[] , (-1, 1)]
}

def manhattanDistance(v, u):
    x1, y1 = graph[v][1]
    x2, y2 = graph[u][1]
    return abs(x2 - x1) + abs(y2 - y1)

def euclideanDistance(v, u):
    x1, y1 = graph[v][1]
    x2, y2 = graph[u][1]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def successors(node):
    return graph[node][0]

def bestFirstSearch(graph, start, goal, heuristic):
    openList = [(start, 0)]
    closedList = []
    
    while openList:
        openList.sort(key=lambda x: x[1])
        current, _ = openList.pop(0)
        closedList.append(current)

        if current == goal:
            return closedList
        
        for neighbor in successors(current):
            if neighbor not in openList and neighbor not in closedList:
                if heuristic == "manhattan":
                    openList.append((neighbor, manhattanDistance(neighbor, start)))
                elif heuristic == "euclidean":
                    openList.append((neighbor, euclideanDistance(neighbor, start)))

def printPath():
    try:
        start = 'S'
        goal = 'I' 
        heuristic = "euclidean"
        path = bestFirstSearch(graph, start, goal, heuristic)
        print("Start:", start)
        print("Goal:", goal)
        
        if heuristic == "manhattan":
            print("Heuristic: Manhattan Distance")
        elif heuristic == "euclidean":
            print("Heuristic: Euclidean Distance")    
        
        print("Path:", path)
        totalCost = 0
        for j in range(len(path) - 1):
            for k in graph[path[j]][0]:
                if k == path[j + 1]:
                    totalCost += 1  # Assuming edge costs are 1
        print("Total Cost:", totalCost)

        # Draw and save the graph
        drawGraph(graph, path, save_path="AI_Assignments/Assignment4/graphBestFirst.png")
        
    except Exception as e:
        print("Path not possible:", str(e))

def drawGraph(graph, path, save_path=None):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for edge in neighbors[0]:
            G.add_edge(node, edge)

    pos = {node: graph[node][1] for node in graph}
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='black')
    
    # Highlight the path
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    if save_path:
        plt.savefig(save_path, format="PNG")  # Save the figure as a PNG image
    else:
        plt.show()

printPath()