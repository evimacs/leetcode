class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right and root.val == target:
            return True

        target -= root.val
        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right,
                                                                     target)


def main():
    tree = TreeNode(5, left=TreeNode(4, left=TreeNode(11, left=TreeNode(7),
                                                      right=TreeNode(2))),
                    right=TreeNode(8, left=TreeNode(13),
                                   right=TreeNode(4, right=TreeNode(1))))
    solution = Solution()
    ret = solution.hasPathSum(tree, 18)
    print(ret)


if __name__ == '__main__':
    main()
