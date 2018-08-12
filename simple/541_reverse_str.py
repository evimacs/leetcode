class Solution(object):
    def reverseStr(self, s, k):
        """

        :type s: str
        :type k: int
        :rtype: str
        """
        rets = ''
        for i in range(0, len(s) // (2 * k) + 1):
            ret = s[i * 2 * k: (i + 1) * 2 * k]
            rets = rets + ret[k - 1::-1] + ret[k::]
        return rets


def main():
    solution = Solution()
    ret = solution.reverseStr('abcdefg', 2)
    print(ret)


if __name__ == '__main__':
    main()
