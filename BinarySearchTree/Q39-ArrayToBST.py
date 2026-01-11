''' Array to BST:
Given a sorted array. Convert it into a Height Balanced Binary Search Tree (BST). Find the preorder traversal of height-balanced BST. If there exist many such balanced BST consider the tree whose preorder is lexicographically smallest.

Example

Input: array = {1, 2, 3, 4}
Output: {2, 1, 3, 4}
'''
class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to convert sorted array to BST
def sortedArrayToBST(arr, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    root = newNode(arr[mid])

    root.left = sortedArrayToBST(arr, start, mid - 1)
    root.right = sortedArrayToBST(arr, mid + 1, end)

    return root

# Function to create a new node with given data
def newNode(data):
    node = TNode(data)
    return node

# Function to perform pre-order traversal of the tree
def preOrder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)

if __name__ == "__main__":
    # Example usage
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(arr)

    root = sortedArrayToBST(arr, 0, n - 1)

    print("Preorder Traversal of constructed BST:")
    preOrder(root)
    print()