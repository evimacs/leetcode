class Solution(object):
    def idUgly(self, num):
        """

        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        while True:
            if not num % 2:
                num = num // 2
                continue
            if not num % 3:
                num = num // 3
                continue
            if not num % 5:
                num = num // 5
                continue
            if num <= 1:
                return True
            return False


def main():
    solution = Solution()
    ret = solution.idUgly(6)
    print(ret)


if __name__ == '__main__':
    main()
