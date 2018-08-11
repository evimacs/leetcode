class Solution:
    def covertToTitle(self, n):
        """

        :type n: int
        :rtype: str
        """
        ret = ''
        while n > 26:

            ret += chr(64 + n % 26)
            n = n // 26

        ret += chr(64 + n)
        ret = ret[::-1]
        return ret

def main():
    solution = Solution()
    ret = solution.covertToTitle(701)
    print(ret)

if __name__ == '__main__':
    main()