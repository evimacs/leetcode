class Solution(object):
    def findDisappearedNumbers(self, nums):
        """

        :type nums: list[int]
        :rtype: list[int]
        """
        return list(set(range(1, len(nums) + 1)) - set(nums))


def main():
    solution = Solution()
    ret = solution.findDisappearedNumbers([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
