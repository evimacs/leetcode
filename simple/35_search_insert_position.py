class Solution(object):
    def searchInsert(self, nums, target):
        """

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for x, y in enumerate(nums):
            if y >= target:
                return x
        return len(nums)


def main():
    solution = Solution()
    ret = solution.searchInsert([1, 3, 5, 6], 5)
    print(ret)
    ret = solution.searchInsert([1, 3, 5, 6], 2)
    print(ret)
    ret = solution.searchInsert([1, 3, 5, 6], 7)
    print(ret)
    ret = solution.searchInsert([1, 3, 5, 6], 0)
    print(ret)


if __name__ == '__main__':
    main()
