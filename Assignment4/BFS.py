class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, node, neighbors):
        self.graph[node] = neighbors

    def BFS(self, start):
        visited = []
        queue = []

        visited.append(start)
        queue.append(start)

        while queue:
            currentNode = queue.pop(0)
            print(currentNode, end=" ")

            for neighbor in self.graph[currentNode]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

    def isPathExists(self, start, end):
        visited = []
        queue = []

        visited.append(start)
        queue.append(start)

        while queue:
            currentNode = queue.pop(0)

            if currentNode == end:
                return True

            for neighbor in self.graph[currentNode]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

        return False

# Usage
if __name__ == "__main__":
    graph = Graph()
    graph.addEdge('5', ['3', '7'])
    graph.addEdge('3', ['2', '4'])
    graph.addEdge('7', ['8'])
    graph.addEdge('2', [])
    graph.addEdge('4', ['8'])
    graph.addEdge('8', [])

    print("Following is the Breadth-First Search:")
    graph.BFS('5')

    startNode = '5'
    endNode = '8'
    if graph.isPathExists(startNode, endNode):
        print(f"\nPath exists between {startNode} and {endNode}")
    else:
        print(f"\nNo path exists between {startNode} and {endNode}")