class Solution(object):
    def titleToNumber(self, s):
        """

        :type s: str
        :rtype: int
        """
        flag = len(s)
        ret = 0
        for x in s:
            flag -= 1
            ret += (ord(x) - 64) * pow(26, flag)
        return ret

def main():
    solution = Solution()
    ret = solution.titleToNumber('AAAAAA')
    print(ret)

if __name__ == '__main__':
    main()