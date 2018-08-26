class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        a = list(zip(*ops))
        return min(a[0]) * min(a[1])



def main():
    solution = Solution()
    ret = solution.maxCount([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
