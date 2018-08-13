class Solution(object):
    def findMaxAverage(self, nums, k):
        """

        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ret = 0
        a = 0
        for x in range(len(nums) - k + 1):
            _ret = sum(nums[x:(x + k):])
            if not a:
                ret = _ret
            if ret < _ret:
                ret = _ret
            a += 1
        return ret  / k


def main():
    solution = Solution()
    ret = solution.findMaxAverage([-1], 1)
    print(ret)


if __name__ == '__main__':
    main()
