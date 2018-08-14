class Solution(object):
    def arrayPairSum(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[0::2])


def main():
    solution = Solution()
    ret = solution.arrayPairSum()
    print(ret)


if __name__ == '__main__':
    main()
