def guess(n):
    return 1


class Solution(object):
    def guessNumber(self, n):
        """

        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while True:
            middle = (start + end) / 2
            op_code = guess(middle)
            if op_code == -1:
                end = middle - 1
            elif op_code == 1:
                start = middle + 1
            else:
                return middle


def main():
    solution = Solution()
    ret = solution.guessNumber()
    print(ret)


if __name__ == '__main__':
    main()
