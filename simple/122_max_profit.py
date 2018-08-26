class Solution(object):
    def maxProfit(self, prices):
        """

        :type prices: list[int]
        :rtype: int
        """
        profit = 0
        i = 0
        while i < len(prices) - 1:
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
            i += 1

        return profit


def main():
    solution = Solution()
    ret = solution.maxProfit([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
