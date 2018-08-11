class Solution(object):
    def moveZeroes(self, nums):
        """

        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead
        """
        _count = nums.count(0)
        for x in range(_count):
            nums.remove(0)
        nums.extend([0] * _count)


def main():
    solution = Solution()
    ret = solution.moveZeroes()
    print(ret)


if __name__ == '__main__':
    main()
