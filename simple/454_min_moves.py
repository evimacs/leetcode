class Solution(object):
    def minMoves(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        min_ele = min(nums)
        return sum([num - min_ele for num in nums])


def main():
    solution = Solution()
    ret = solution.minMoves([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
