class Solution(object):
    def longestPalindrome(self, s):
        """

        :type s: str
        :rtype: int
        """
        ret = 0
        temp = list()
        for x in set(s):
            ret += s.count(x) // 2 * 2
            if s.count(x) % 2 and not temp:
                temp.append(x)
        return ret + len(temp)


def main():
    solution = Solution()
    ret = solution.longestPalindrome('abccccdd')
    print(ret)


if __name__ == '__main__':
    main()
