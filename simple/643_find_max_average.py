class Solution(object):
    def findMaxAverage(self, nums, k):
        """

        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ret = 0
        a = 0
        max_sum = sum(nums[0:k])
        now_sum = sum(nums[0:k])
        for x in range(1, len(nums) - k + 1):
            now_sum = now_sum - nums[x - 1] + nums[x + k - 1]
            if max_sum < now_sum:
                max_sum = now_sum
        return max_sum / k


def main():
    solution = Solution()
    ret = solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
    print(ret)


if __name__ == '__main__':
    main()
