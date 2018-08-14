class Solution(object):
    def dominantIndex(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        nums1 = list(sorted(list(set(nums))))
        if nums1[-1] >= nums1[-2] * 2:
            return nums.index(nums1[-1])
        else:
            return -1


def main():
    solution = Solution()
    ret = solution.dominantIndex()
    print(ret)


if __name__ == '__main__':
    main()
