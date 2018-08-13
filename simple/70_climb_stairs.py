class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in (1, 0):
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


def main():
    solution = Solution()
    ret = solution.climbStairs(4)
    print(ret)


if __name__ == '__main__':
    main()

