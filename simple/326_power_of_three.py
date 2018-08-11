class Solution(object):
    def isPowerOfThree(self, n):
        """

        :type n: List[int]
        :rtype: bool
        """

        if n == 1:
            return True
        elif (n / 3) != (n // 3) or n < 1:
            return False
        else:
            return self.isPowerOfThree(n / 3)


def main():
    solution = Solution()
    ret = solution.isPowerOfThree(27)
    print(ret)


if __name__ == '__main__':
    main()
