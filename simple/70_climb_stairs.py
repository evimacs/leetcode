class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = [0] * (n + 1)
        ret[0:2] = [1, 1]
        for i in range(2, n + 1):
            ret[i] = ret[i - 1] + ret[i - 2]
        return ret[n]


def main():
    solution = Solution()
    ret = solution.climbStairs(4)
    print(ret)


if __name__ == '__main__':
    main()
