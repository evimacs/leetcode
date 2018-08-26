class Solution(object):
    def letterCasePermutation(self, s):
        """

        :type s: str
        :rtype: List[str]
        """
        ret = set()
        ret.add(s)
        for y, x in enumerate(s):
            if x.isupper():
                ret.add(s[0:y] + x.lower() + s[y + 1:])
            elif x.islower():
                ret.add(s[0:y] + x.upper() + s[y + 1:].lower())
            ret.add(s[0:y] + x + s[y + 1:].lower())
        return list(ret)


def main():
    solution = Solution()
    ret = solution.letterCasePermutation('a1b2')
    print(ret)


if __name__ == '__main__':
    main()

