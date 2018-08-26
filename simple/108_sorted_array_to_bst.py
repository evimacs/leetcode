class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBst(self, nums):
        """

        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None
        root = TreeNode(nums[len(nums) // 2])
        root.left = self.sortedArrayToBst(nums[:len(nums) // 2])
        root.right = self.sortedArrayToBst(nums[(len(nums) // 2 + 1):])
        return root


def main():
    solution = Solution()
    ret = solution.sortedArrayToBst()
    print(ret)


if __name__ == '__main__':
    main()
