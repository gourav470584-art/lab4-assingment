# dmmt_toolkit.py

# ---------------- BST IMPLEMENTATION ----------------
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.key)
            self._inorder(root.right, result)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None
            # Case 2: One child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Case 3: Two children
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current


# ---------------- GRAPH IMPLEMENTATION ----------------
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def print_graph(self):
        for node in self.graph:
            print(node, "->", self.graph[node])

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        print("BFS:", end=" ")
        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbour, _ in self.graph.get(node, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        print()

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for neighbour, _ in self.graph.get(start, []):
            if neighbour not in visited:
                self.dfs(neighbour, visited)


# ---------------- MAIN FUNCTION ----------------
def main():
    print("----- BST OPERATIONS -----")
    bst = BST()

    data = [50, 30, 70, 20, 40, 60, 80]
    for x in data:
        bst.insert(x)

    print("Inorder:", bst.inorder())

    print("Search 20:", bst.search(20))
    print("Search 90:", bst.search(90))

    # Delete leaf node
    bst.delete(20)
    print("After deleting 20:", bst.inorder())

    # One child case
    bst.insert(65)
    bst.delete(60)
    print("After deleting 60:", bst.inorder())

    # Two children case
    bst.delete(30)
    print("After deleting 30:", bst.inorder())

    # ---------------- GRAPH ----------------
    print("\n----- GRAPH -----")
    g = Graph()

    edges = [
        ('A', 'B', 2), ('A', 'C', 4),
        ('B', 'D', 7), ('B', 'E', 3),
        ('C', 'E', 1), ('D', 'F', 5),
        ('E', 'D', 2), ('E', 'F', 6),
        ('C', 'F', 8)
    ]

    for u, v, w in edges:
        g.add_edge(u, v, w)

    print("Adjacency List:")
    g.print_graph()

    g.bfs('A')

    print("DFS:", end=" ")
    g.dfs('A')
    print()


if __name__ == "__main__":
    main()
