class Solution(object):
    def findAnagrams(self, s, p):
        """

        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_len = len(p)
        set_p = set(p)
        ret = list()
        for i in range(len(s) - p_len + 1):
            for _p in set_p:
                if s[i:i + p_len].count(_p) != p.count(_p):
                    break
            else:
                ret.append(i)
        return list(ret)


def main():
    solution = Solution()
    ret = solution.findAnagrams('ababababab', 'aab')
    print(ret)


if __name__ == '__main__':
    main()
