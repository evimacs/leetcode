class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """

        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ret = list()
        temp = 0
        for x in flowerbed:
            if x == 0:
                temp += 1
            else:
                if temp and temp >= 3:
                    ret.append(temp)
                temp = 0
        return sum(ret) >= (2 * n + 1)


def main():
    solution = Solution()
    ret = solution.canPlaceFlowers([1, 0, 0, 0, 1], 1)
    print(ret)


if __name__ == '__main__':
    main()
