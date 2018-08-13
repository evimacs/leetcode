class Solution(object):
    def hammingWeight(self, n):
        """

        :type n:
        :rtype: int
        """
        return str(bin(n)).count('1')


def main():
    solution = Solution()
    ret = solution.hammingWeight([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
