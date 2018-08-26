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

        def f(p, q):
            if not p:
                return not q
            if not q:
                return not p
            if p.val == q.val:
                return f(p.left, q.right) and f(p.right, q.left)
            if p.val != q.val:
                return False

        if not root:
            return True
        return f(root.right, root.left)


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
