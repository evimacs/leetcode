class Solution(object):
    def trailingZeroes(self, n):
        """

        :type n: int
        :rtype: int
        """
        ret = 0
        while n >= 5:
            n = n // 5
            ret += n
        return ret

def main():
    solution = Solution()
    ret = solution.trailingZeroes(30)
    print(ret)

if __name__ == '__main__':
    main()