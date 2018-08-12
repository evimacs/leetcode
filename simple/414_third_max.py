class Solution(object):
    def thirdMax(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        ret = list(sorted(set(nums)))
        return ret[-3] if len(ret) >= 3 else ret[-1]


def main():
    solution = Solution()
    ret = solution.thirdMax()
    print(ret)


if __name__ == '__main__':
    main()
