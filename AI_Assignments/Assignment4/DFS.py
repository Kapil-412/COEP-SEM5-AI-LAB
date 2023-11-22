import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, node, neighbors):
        self.graph[node] = neighbors

    def draw_graph(self, save_path=None):  # Added save_path parameter
        G = nx.Graph()

        for node, neighbors in self.graph.items():
            for edge in neighbors:
                G.add_edge(node, edge)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='black')

        if save_path:
            plt.savefig(save_path, format="PNG")  # Save the figure as a PNG image
        else:
            plt.show()

    def DFS(self, start):
        visited = set()
        self.dfsRecursive(start, visited)

    def dfsRecursive(self, node, visited):
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in self.graph[node]:
                self.dfsRecursive(neighbour, visited)

    def isPathExists(self, start, end, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)

        if start == end:
            return True

        for neighbour in self.graph[start]:
            if neighbour not in visited and self.isPathExists(neighbour, end, visited):
                return True

        return False

# Usage
if __name__ == "__main__":
    graph = Graph()
    graph.addEdge('5', ['3', '7'])
    graph.addEdge('3', ['2', '4'])
    graph.addEdge('7', ['8', '4'])
    graph.addEdge('2', ['5', '7'])
    graph.addEdge('4', ['8'])
    graph.addEdge('8', [])

    graph.draw_graph(save_path="AI_Assignments/Assignment4/graphDFS.png")  # Specify the save_path to save the image
    print("Following is the Depth-First Search:")
    graph.DFS('5')

    startNode = '5'
    endNode = '8'
    if graph.isPathExists(startNode, endNode):
        print(f"\nPath exists between {startNode} and {endNode}")
    else:
        print(f"\nNo path exists between {startNode} and {endNode}")