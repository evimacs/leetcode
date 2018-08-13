class Solution:
    def covertToTitle(self, n):
        """

        :type n: int
        :rtype: str
        """
        ret = ''
        while n > 0:
            print(n)
            ret += chr(ord('A') + (n-1) % 26)
            n = (n-1) // 26
        return ret[::-1]

def main():
    solution = Solution()
    ret = solution.covertToTitle(701)
    print(ret)

if __name__ == '__main__':
    main()
