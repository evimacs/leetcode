class Solution(object):
    def judgeSquareSum(self, c):
        """

        :type c: int
        :rtype: bool
        """
        if int(c ** 0.5) == c ** 0.5:
            return True
        high = int(c ** 0.5) + 1
        low = 1
        while low <= high:
            if low ** 2 + high ** 2 > c:
                high -= 1
            elif low ** 2 + high ** 2 < c:
                low += 1
            else:
                return True
        return False


def main():
    solution = Solution()
    ret = solution.judgeSquareSum()
    print(ret)


if __name__ == '__main__':
    main()
