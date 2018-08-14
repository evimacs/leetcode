class Solution(object):
    def validPalindrome(self, s):
        """

        :type s: str
        :rtype: bool
        """
        ret = s[::-1]
        if s == ret:
            return True
        k = len(s)
        for i in range(k):
            if s[i] != s[k - i - 1]:
                s1 = s[i:k - i - 1]
                s2 = s[i + 1:k - i]
                return s1 == s1[::-1] or s2 == s2[::-1]
        return True


def main():
    solution = Solution()
    ret = solution.validPalindrome('abca')
    print(ret)


if __name__ == '__main__':
    main()
