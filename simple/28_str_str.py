class Solution(object):
    def strStr(self, haystack, needle):
        """

        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for x in range(len(haystack)):
            if x + len(needle) > len(haystack):
                return -1
            if haystack[x:x + len(needle):] == needle:
                return x
        return -1


def main():
    solution = Solution()
    ret = solution.strStr()
    print(ret)


if __name__ == '__main__':
    main()
