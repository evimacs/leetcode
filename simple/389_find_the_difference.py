class Solution(object):
    def findTheDifference(self, s, t):
        """

        :type s: str
        :type t: str
        :rtype: str
        """
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        try:
            for x in range(len(t)):
                if t[x] != s[x]:
                    return t[x]
        except Exception:
            return t[-1]


def main():
    solution = Solution()
    ret = solution.findTheDifference()
    print(ret)


if __name__ == '__main__':
    main()
