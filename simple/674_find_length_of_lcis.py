class Solution(object):
    def findLengthOfLCIS(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        N = len(nums)
        Dp = [1] * N
        for i in range(N - 1):
            for j in range(0, i + 1):
                if nums[i + 1] > nums[j]:
                    Dp[i + 1] = max(Dp[i + 1], Dp[j] + 1)
        return max(Dp)


def main():
    solution = Solution()
    ret = solution.findLengthOfLCIS([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
