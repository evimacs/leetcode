class Solution(object):
    def missingNumber(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        return int((n * (n - 1) / 2) - sum(nums))


def main():
    solution = Solution()
    ret = solution.missingNumber([3, 0, 1])
    print(ret)


if __name__ == '__main__':
    main()
