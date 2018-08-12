class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        _flag = 0
        flag = 0
        for x in nums:
            if x == 1:
                flag += 1
            else:
                _flag = max(flag, _flag)
                flag = 0
        return max(_flag, flag)


def main():
    solution = Solution()
    ret = solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])
    print(ret)


if __name__ == '__main__':
    main()
