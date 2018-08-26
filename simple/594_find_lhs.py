class Solution(object):
    def findLHS(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        temp = dict()
        for x in nums:
            if x in temp:
                temp[x] += 1
            else:
                temp[x] = 1
        for x in temp:
            if x + 1 in temp:
                _len = temp[x] + temp[x + 1]
                if _len > max_len:
                    max_len = _len
        return max_len


def main():
    solution = Solution()
    ret = solution.findLHS([1, 3, 2, 2, 5, 2, 3, 7])
    print(ret)


if __name__ == '__main__':
    main()
