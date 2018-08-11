class Solution(object):
    def plusOne(self, dights):
        """

        :type dights: List[int]
        :rtype: List[int]
        """
        for i in range(len(dights) - 1, -1, -1):
            if dights[i] + 1 < 10:
                dights[i] += 1
                return dights
            else:
                dights[i] = 0
        dights.insert(0, 1)
        return dights


def main():
    solution = Solution()
    ret = solution.plusOne([9, 9, 9])
    print(ret)


if __name__ == '__main__':
    main()
