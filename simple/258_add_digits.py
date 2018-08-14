class Solution(object):
    def addDigits(self, num):
        """

        :type num: int
        :rtype: int
        """
        return num and (num % 9 or 9)


def main():
    solution = Solution()
    ret = solution.addDigits()
    print(ret)


if __name__ == '__main__':
    main()
