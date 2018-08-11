class Solution(object):
    def isPowerOfFour(self, n):
        """

        :type n: List[int]
        :rtype: bool
        """
        if n == 1:
            return True
        elif (n / 4) != (n // 4) or n < 1:
            return False
        else:
            return self.isPowerOfFour(n / 4)


def main():
    solution = Solution()
    ret = solution.isPowerOfFour(64)
    print(ret)


if __name__ == '__main__':
    main()
