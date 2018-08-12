class Solution(object):
    def numJewelsInStones(self, J, S):
        """

        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([1 for x in S if x in J])


def main():
    solution = Solution()
    ret = solution.numJewelsInStones()
    print(ret)


if __name__ == '__main__':
    main()
