class Solution(object):
    def countBinarySubStrings(self, s):
        """

        :type s: str
        :rtype: int
        """
        L = list(
            map(len, s.replace('01', '0 1').replace('10', '1 0').split(' ')))
        return sum(min(a, b) for a, b in zip(L, L[1:]))


def main():
    solution = Solution()
    ret = solution.countBinarySubStrings()
    print(ret)


if __name__ == '__main__':
    main()
