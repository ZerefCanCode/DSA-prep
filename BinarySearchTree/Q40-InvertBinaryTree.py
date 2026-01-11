'''Invert Binary Tree:
Given the root of a binary tree, invert the tree, and return its root.'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
       
        left_subtree = self.invertTree(root.left)
        right_subtree = self.invertTree(root.right)
       
        root.left = right_subtree
        root.right = left_subtree
       
        return root
   
    def printPreorder(self, root: TreeNode) -> None:
        if root is None:
            return
        print(root.val, end=' ')
        self.printPreorder(root.left)
        self.printPreorder(root.right)

if __name__ == "__main__":
    # Example usage with the provided input
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    sol = Solution()
   
    print("Preorder Traversal of Original Tree:", end=' ')
    sol.printPreorder(root)
    print()
   
    inverted_tree = sol.invertTree(root)

    print("Preorder Traversal of Inverted Tree:", end=' ')
    sol.printPreorder(inverted_tree)  # Output: 4 7 9 6 2 3 1
    print()
