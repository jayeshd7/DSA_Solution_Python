from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeZigZag:
    def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        left_to_right = True
        while queue:
            level_size = len(queue)
            level = []
            for i in range(level_size):
                node = queue.pop(0)
                if left_to_right:
                    level.append(node.val)
                else:
                    level = [node.val] + level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
            left_to_right = not left_to_right

        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(4)
    bt = BinaryTreeZigZag
    print(bt.zigzagLevelOrder(root))
