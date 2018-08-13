class Solution(object):
    def validPalindrome(self, s):
        """

        :type s: str
        :rtype: bool
        """
        ret = s[::-1]
        if s == ret:
            return True

        for i in range(len(s)):
            print(s)
            if s[i] != ret[i]:
                print(i)
                temp = s[:i:] + s[:i+1:]
                print(temp)
                return temp == temp[::-1]



def main():
    solution = Solution()
    ret = solution.validPalindrome('abca')
    print(ret)


if __name__ == '__main__':
    main()
