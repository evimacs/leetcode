class Solution(object):
    def findMaxAverage(self, nums, k):
        """

        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        averages = list()
        if len(nums) == k:
            return sum(nums) / k
        for x in range(len(nums) - k):
            averages.append(sum(nums[x: x + k]) / k)
        return max(averages)


def main():
    solution = Solution()
    ret = solution.findMaxAverage([5, 5], 1)
    print(ret)


if __name__ == '__main__':
    main()
