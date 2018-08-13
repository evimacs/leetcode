class Solution(object):
    def findDuplicate(self, nums):
        """

        :type nums: List[int]
        :rtype: bool
        """
        nums1 = set(nums)
        return (sum(nums) - sum(nums1)) // (len(nums) - len(nums1))


def main():
    solution = Solution()
    ret = solution.findDuplicate([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
