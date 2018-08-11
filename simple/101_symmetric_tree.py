class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def isSymetric(self, root):
        """

        :type root:TreeNode
        :rtype: bool
        """
        if root.right.right.val == root.left.left.val and root.right.left.val == root.left.right.val:
            return True
        return self.isSymetric(root)


def main():
    tree = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                    right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
    solution = Solution()
    ret = solution.isSymetric(tree)
    print(ret)
    tree = TreeNode(1, left=TreeNode(2, right=TreeNode(3)),
                    right=TreeNode(2, right=TreeNode(3)))
    solution = Solution()
    ret = solution.isSymetric(tree)
    print(ret)

if __name__ == '__main__':
    main()
