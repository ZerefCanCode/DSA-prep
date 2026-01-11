#Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(node, res):
    if not node:
        return

    # Visit the current node first
    res.append(node.data)

    # Traverse the left subtree
    preOrder(node.left, res)

    # Traverse the right subtree
    preOrder(node.right, res)

if __name__ == "__main__":
    
    # Create binary tree
    #       1
    #      /  \
    #    2     3
    #   / \     \
    #  4   5     6
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    
    result = []
    preOrder(root, result)

    for node in result:
        print(node, end=" ")
    print()