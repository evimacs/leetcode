class Solution(object):
    def isPalindrome(self, s):
        """

        :type s:str
        :rtype: bool
        """
        temp = ''
        for x in s:
            if x.isalpha():
                temp += x.lower()
            elif x.isdigit():
                temp += x
        return temp == temp[::-1]


def main():
    solution = Solution()
    ret = solution.isPalindrome('A man, a plan, a canal: Panama')
    print(ret)
    ret = solution.isPalindrome('race a car')
    print(ret)
if __name__ == '__main__':
    main()