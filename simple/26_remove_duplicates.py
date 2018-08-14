class Solution(object):
    def removeDuplicates(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        for x in nums[::-1]:
            if x == temp:
                nums.remove(x)
            else:
                temp = x
        return len(nums)


def main():
    solution = Solution()
    ret = solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(ret)


if __name__ == '__main__':
    main()
