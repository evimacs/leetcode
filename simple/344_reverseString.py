class Solution(object):
    def reverString(self, s):
        """

        :type s: str
        :rtype: str
        """
        return s[::-1]


def main():
    solution = Solution()
    ret = solution.reverString('abc')
    print(ret)


if __name__ == '__main__':
    main()
