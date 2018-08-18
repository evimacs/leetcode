class Solution(object):
    def findPairs(self, nums, k):
        """

        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k < 0 or not nums:
            return 0
        temp = dict()
        for x in nums:
            if x not in temp:
                temp[x] = 1
            else:
                temp[x] += 1
        ret = 0
        if k == 0:
            for v in temp.values():
                if v > 1:
                    ret += 1
        else:
            for x in temp:
                if x + k in temp:
                    ret += 1
        return ret

def main():
    solution = Solution()
    ret = solution.findPairs([1, 3, 1, 5, 4], 2)
    print(ret)


if __name__ == '__main__':
    main()
