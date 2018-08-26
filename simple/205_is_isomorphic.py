class Solution(object):
    def isIsomorphic(self, s, t):
        """

        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        temp1 = dict()
        temp2 = dict()
        for x in range(len(s)):
            if s[x] in temp1:
                if temp1[s[x]] != t[x]:
                    return False
            else:
                temp1[s[x]] = t[x]
            if t[x] in temp2:
                if temp2[t[x]] != s[x]:
                    return False
            else:
                temp2[t[x]] = s[x]
        return True


def main():
    solution = Solution()
    ret = solution.isIsomorphic('ab', 'aa')
    print(ret)


if __name__ == '__main__':
    main()
