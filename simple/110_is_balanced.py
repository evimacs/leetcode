class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """

        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        elif abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if root == None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1


def main():
    solution = Solution()
    ret = solution.isBalanced()
    print(ret)


if __name__ == '__main__':
    main()
