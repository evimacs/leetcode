class Solution(object):
    def repeatedStringMatch(self, A, B):
        """

        :type A: str
        :type B: str
        :rtype: int
        """
        temp = ''
        flag = 0
        while len(temp) < len(B):
            temp += A
            flag += 1
        if B in temp:
            return flag
        temp += A
        if B in temp:
            return flag + 1
        else:
            return -1


def main():
    solution = Solution()
    A = 'abcd'
    B = 'cdabcdab'
    ret = solution.repeatedStringMatch(A, B)
    print(ret)


if __name__ == '__main__':
    main()
