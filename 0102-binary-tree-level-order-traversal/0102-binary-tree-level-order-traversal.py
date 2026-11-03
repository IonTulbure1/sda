
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        rezultat = []
        queue = [root]

        while len(queue) > 0:
            nivel = []
            urmator = []

            for nod in queue:
                nivel.append(nod.val)

                if nod.left is not None:
                    urmator.append(nod.left)

                if nod.right is not None:
                    urmator.append(nod.right)

            rezultat.append(nivel)
            queue = urmator

        return rezultat
