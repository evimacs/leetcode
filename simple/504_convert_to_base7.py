class Solution(object):
    def convertToBase7(self, num):
        """

        :type num: int
        :rtype: str
        """
        if not num:
            return str(num)
        ret = ''
        flag = num // abs(num)
        num = abs(num)
        while num >= 7:
            ret += str(num % 7)
            num //= 7
        ret += str(num)
        return str(int(ret[::-1]) * flag)


def main():
    solution = Solution()
    ret = solution.convertToBase7(100)
    print(ret)


if __name__ == '__main__':
    main()
