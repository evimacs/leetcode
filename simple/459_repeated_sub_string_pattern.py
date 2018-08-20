class Solution(object):
    def repeatedSubstringPattern(self, s):
        """

        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i:
                continue
            temp = s[:i]
            if temp * (len(s) // i) == s:
                return True
        return False



def main():
    solution = Solution()
    ret = solution.repeatedSubstringPattern('abcabcabcabc')
    print(ret)


if __name__ == '__main__':
    main()
