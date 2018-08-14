class Solution(object):
    def arrangeCoins(self, n):
        """

        :type n: int
        :rtype: int
        """

        low = 0
        high = n
        while low <= high:
            mid = int((low + high) / 2)
            if 0 <= n - (mid + 1) * mid / 2 < mid + 1:
                return mid
            elif n - (mid + 1) * mid / 2 > 0:
                low = mid + 1
            elif n - (mid + 1) * mid / 2 < 0:
                high = mid - 1


def main():
    solution = Solution()
    ret = solution.arrangeCoins(8)
    print(ret)


if __name__ == '__main__':
    main()
