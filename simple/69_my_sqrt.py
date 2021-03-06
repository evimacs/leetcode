class Solution(object):
    def mySqrt(self, x):
        """

        :type x: int
        :rtype: int
        """

        start = 0
        end = x
        middle = (start + end) // 2
        while start <= end:
            temp = middle * middle
            if temp > x:
                end = middle - 1
            elif temp < x:
                start = middle + 1
            else:
                return middle
            middle = (start + end) // 2
        return middle


def main():
    solution = Solution()
    ret = solution.mySqrt(8)
    print(ret)


if __name__ == '__main__':
    main()
