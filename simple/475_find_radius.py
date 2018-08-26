class Solution(object):
    def findRadius(self, houses, heaters):
        """

        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        maxidx = 0
        index = 0
        for i in range(len(houses)):
            while index + 1 < len(heaters) and (
                    abs(heaters[index + 1] - houses[i]) <= abs(
                    heaters[index] - houses[i])):
                index += 1
            maxidx = max(maxidx, abs(heaters[index] - houses[i]))
        return maxidx


def main():
    solution = Solution()
    ret = solution.findRadius([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
