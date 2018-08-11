class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """

        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left > right:
            return left + 1
        else:
            return right + 1

def main():
    p = TreeNode(1, left=TreeNode(2), right=TreeNode(1))
    q = TreeNode(1, left=TreeNode(1, left=TreeNode(10)), right=TreeNode(2))
    solution = Solution()
    ret = solution.maxDepth(q)
    print(ret)


if __name__ == '__main__':
    main()