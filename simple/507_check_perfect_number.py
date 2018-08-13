import math


class Solution(object):
    def checkPerfectNumber(self, num):
        """

        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        temp = 0
        for x in range(1, int(math.sqrt(num)) + 1):
            if num % x == 0:
                temp += x + ((num // x) if (num // x) < num else 0)
        return num == temp


def main():
    solution = Solution()
    ret = solution.checkPerfectNumber(28)
    print(ret)


if __name__ == '__main__':
    main()

