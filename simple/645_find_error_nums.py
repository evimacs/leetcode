class Solution(object):
    def findErrorNums(self, nums):
        """

        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        temp1 = list(set(range(1, n + 1)) - set(nums))
        temp2 = sum(nums) - sum(set(nums))
        temp1.insert(0, temp2)
        return temp1


def main():
    solution = Solution()
    ret = solution.findErrorNums([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
