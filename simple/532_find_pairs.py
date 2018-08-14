class Solution(object):
    def findPairs(self, nums, k):
        """

        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        temp = set()
        nums = set(nums)
        for x in nums:
            if (x + k) in nums:
                temp.add((x, x + k))
            if (x - k) in nums:
                temp.add((x - k, x))
        print(temp)

        return len(temp)


def main():
    solution = Solution()
    ret = solution.findPairs([1, 3, 1, 5, 4], 0)
    print(ret)


if __name__ == '__main__':
    main()
