class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums = nums[k+1::] + nums[:k+1:]
        print(nums)


def main():
    solution = Solution()
    ret = solution.rotate([1,2,3,4,5,6,7], 3)
    print(ret)


if __name__ == '__main__':
    main()
