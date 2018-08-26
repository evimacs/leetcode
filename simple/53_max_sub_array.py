class Solution(object):
    def maxSubArray(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                sum = 0
        return max_sum


def main():
    solution = Solution()
    ret = solution.maxSubArray([-2, -1, -3, -4, -1, -2, -1, -5, -4])
    print(ret)


if __name__ == '__main__':
    main()
