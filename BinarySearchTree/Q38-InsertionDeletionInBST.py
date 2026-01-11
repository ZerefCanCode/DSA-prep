class Tree:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root is None:
        return

    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)

def insert_node(root, x):
    if root is None:
        return Tree(x)

    if root.data > x:
        root.left = insert_node(root.left, x)
    else:
        root.right = insert_node(root.right, x)

    return root

def delete_node(root, x):
    if root is None:
        print("Node not found")
        return None

    if root.data > x:
        root.left = delete_node(root.left, x)
    elif root.data < x:
        root.right = delete_node(root.right, x)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            temp = root.right
            while temp.left is not None:
                temp = temp.left

            root.data = temp.data
            root.right = delete_node(root.right, temp.data)

    return root

if __name__ == "__main__":
    root = Tree(15)
    root.left = Tree(12)
    root.right = Tree(54)
    root.left.left = Tree(8)
    root.left.right = Tree(13)
    root.left.left.left = Tree(5)
    root.right.left = Tree(20)
    
    x = 10
    insert_node(root, x)
    
    print("Inorder Traversal - ", end="")
    inorder_traversal(root)
    print()
    first_delete = 8
    print("8 deleted")
    root = delete_node(root, first_delete)
    print("Inorder Traversal - ", end="")
    inorder_traversal(root)