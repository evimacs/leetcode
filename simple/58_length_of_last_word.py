class Solution(object):
    def lengthOfLastWord(self, s):
        """

        :type s: str
        :rtype: int
        """
        ret = 0
        for x in s:
            if x == ' ':
                ret = 0
            else:
                ret += 1
        return ret


def main():
    solution = Solution()
    ret = solution.lengthOfLastWord('Hello World')
    print(ret)
    ret = solution.lengthOfLastWord('Hello World ')
    print(ret)
    ret = solution.lengthOfLastWord(' ')
    print(ret)


if __name__ == '__main__':
    main()
