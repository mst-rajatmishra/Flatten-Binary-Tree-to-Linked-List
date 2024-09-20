class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        # Initialize a stack for iterative pre-order traversal
        stack = [root]

        while stack:
            current = stack.pop()

            # If the current node has a right child, push it onto the stack
            if current.right:
                stack.append(current.right)
            # If the current node has a left child, push it onto the stack
            if current.left:
                stack.append(current.left)

            # Rearrange pointers
            current.left = None  # Set left child to None
            if stack:  # If there are more nodes in the stack
                current.right = stack[-1]  # Point right to the next node
