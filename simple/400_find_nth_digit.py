class Solution(object):
    def findNthDigit(self, n):
        """

        :type n: int
        :rtype: int
        """
        temp = ''

        for x in range(1, n + 1):
            temp += str(x)
            if len(temp) >= n:
                return int(temp[n - 1])


def main():
    solution = Solution()
    ret = solution.findNthDigit(3)
    print(ret)


if __name__ == '__main__':
    main()
