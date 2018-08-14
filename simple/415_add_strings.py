class Solution(object):
    def addStrings(self, num1, num2):
        """

        :type num1: str
        :type num2: str
        :rtype: str
        """

        ret = []
        for x in [num1, num2]:
            temp = 0
            for i in x:
                temp = temp * 10 + int(i)
            ret.append(temp)
        return str(ret[0] + ret[1])


def main():
    solution = Solution()
    ret = solution.addStrings('11111', '2222')
    print(ret)


if __name__ == '__main__':
    main()
