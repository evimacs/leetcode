class Solution(object):
    def removeElement(self, nums, val):
        """

        :type nums: List[int]
        :type val: int
        :rtype: List[int]
        """
        while True:
            if val in nums:
                nums.remove(val)
            else:
                break
        return len(nums)


def main():
    solution = Solution()
    ret = solution.removeElement()
    print(ret)


if __name__ == '__main__':
    main()
