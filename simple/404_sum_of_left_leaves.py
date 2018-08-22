class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        super().__init__()
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """

        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(
            root.right)


def main():
    solution = Solution()
    tree = TreeNode(3, left=TreeNode(9),
                    right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    ret = solution.sumOfLeftLeaves(tree)
    print(ret)


if __name__ == '__main__':
    main()
