class Solution(object):
    def maximumProduct(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] * nums[1]
        elif len(nums) == 3:
            return nums[2] * nums[1] * nums[0]
        else:
            return max(nums[-1] * nums[-2] * nums[-3],
                       nums[-1] * nums[0] * nums[1])


def main():
    solution = Solution()
    ret = solution.maximumProduct()
    print(ret)


if __name__ == '__main__':
    main()
