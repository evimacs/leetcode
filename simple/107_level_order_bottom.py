class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        super().__init__()
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrderBottom(self, root):
        """

        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return [[]]
        ret = list()



def main():
    solution = Solution()
    ret = solution.levelOrderBottom([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
