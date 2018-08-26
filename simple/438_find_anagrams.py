class Solution(object):
    def findAnagrams(self, s, p):
        """

        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        p_len = len(p)
        p_set = set(p)
        p_map = dict()
        for x in p_set:
            p_map[x] = p.count(x)
        ret = list()
        temp = set()
        for i in range(len(s) - p_len + 1):
            s1 = s[i:i + p_len]
            if s1 in temp:
                ret.append(i)
                continue
            for x in set(s1):
                if s1.count(x) != p_map.get(x, -1):
                    break
            else:
                ret.append(i)
                temp.add(s1)
        return ret


def main():
    solution = Solution()
    ret = solution.findAnagrams('cbaebabacd', 'abc')
    print(ret)


if __name__ == '__main__':
    main()
