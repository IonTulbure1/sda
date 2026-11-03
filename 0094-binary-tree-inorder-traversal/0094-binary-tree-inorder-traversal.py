
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rezultat = []
        stack = []
        current = root

        while current is not None or len(stack) > 0:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            rezultat.append(current.val)
            current = current.right

        return rezultat
