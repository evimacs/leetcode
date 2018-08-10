class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """

        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif (not q and p) or (not p and q):
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,
                                                                   q.right)


def main():
    p = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    q = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    solution = Solution()
    ret = solution.isSameTree(p, q)
    print(ret)
    p = TreeNode(1, left=TreeNode(2))
    q = TreeNode(1, right=TreeNode(3))
    solution = Solution()
    ret = solution.isSameTree(p, q)
    print(ret)
    p = TreeNode(1, left=TreeNode(2), right=TreeNode(1))
    q = TreeNode(1, left=TreeNode(1), right=TreeNode(2))
    solution = Solution()
    ret = solution.isSameTree(p, q)
    print(ret)


if __name__ == '__main__':
    main()
