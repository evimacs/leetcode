class Solution(object):
    def rotateString(self, A, B):
        """

        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        return B in (A * 2)


def main():
    solution = Solution()
    A = 'abcde'
    B = 'cdeab'
    ret = solution.rotateString(A, B)
    print(ret)
    A = 'abcde'
    B = 'abced'
    ret = solution.rotateString(A, B)
    print(ret)


if __name__ == '__main__':
    main()
