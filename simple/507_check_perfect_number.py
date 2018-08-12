class Solution(object):
    def checkPerfectNumber(self, num):
        """

        :type num: int
        :rtype: bool
        """
        rets = [1]
        for x in range(2, num // 2):
            if num % x == 0:
                rets.extend([x, num // x])
        print(rets)
        return num == sum(set(rets))


def main():
    solution = Solution()
    ret = solution.checkPerfectNumber(28)
    print(ret)


if __name__ == '__main__':
    main()
