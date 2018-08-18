class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        nums[:] = nums[nums_len - k:] + nums[:nums_len - k]


def main():
    solution = Solution()
    ret = solution.rotate([1, 2, 3, 4, 5, 6, 7], 3)
    print(ret)


if __name__ == '__main__':
    main()
