class Solution(object):
    def isPowerOfTwo(self, n):
        """

        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif (n / 2) != (n // 2) or n < 1:
            return False
        else:
            return self.isPowerOfTwo(n / 2)


def main():
    solution = Solution()
    ret = solution.isPowerOfTwo(218)
    print(ret)


if __name__ == '__main__':
    main()
