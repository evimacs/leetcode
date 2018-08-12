class Solution(object):
    def letterCasePermutation(self, s):
        """

        :type s: str
        :rtype: List[str]
        """
        ret = [s]
        temp = list(s)
        a = 0
        for x in s:
            temp[a] = x.lower()
            ret.append(''.join(temp))
            temp[a] = x.upper()
            ret.append(''.join(temp))
        return list(set(ret))


def main():
    solution = Solution()
    ret = solution.letterCasePermutation('a1b2')
    print(ret)


if __name__ == '__main__':
    main()
