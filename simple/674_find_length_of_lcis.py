class Solution(object):
    def findLengthOfLCIS(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        ret = list()
        for i in range(1, len(nums)):
            if i == 1:
                _ret = [nums[0]]
            else:
                _ret = []
            if nums[i] > nums[i - 1]:
                _ret.append(nums[i])
            elif nums[i] < nums[i - 1]:
                ret.append(len(_ret))


def main():
    solution = Solution()
    ret = solution.findLengthOfLCIS([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
