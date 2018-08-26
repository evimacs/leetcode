class Solution(object):
    def findShortestSubArray(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        temp = dict()
        for x in set(nums):
            temp.setdefault(nums.count(x), list()).append(x)
        _nums = nums[::-1]
        s = len(nums)
        min_len = 50000
        for x in temp.get(max(temp.keys())):
            _min_len = s - _nums.index(x) - nums.index(x)
            if _min_len < min_len:
                min_len = _min_len
        return min_len


def main():
    solution = Solution()
    ret = solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])
    print(ret)


if __name__ == '__main__':
    main()
