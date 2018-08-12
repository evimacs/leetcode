class Solution(object):
    def toLowerCase(self, str):
        """

        :type str: str
        :rtype: str
        """
        str1 = ''
        for x in str:
            if x.isalpha() and ord(x) < 97:
                str1 += chr(ord(x) + 32)
            else:
                str1 += x
        return str1


def main():
    solution = Solution()
    ret = solution.toLowerCase()
    print(ret)


if __name__ == '__main__':
    main()
