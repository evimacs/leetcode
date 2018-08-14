def isBadVersion():
    pass


class Solution(object):
    def firstBadVersion(self, n):
        """

        :type n: int
        :rtype: int
        """

        start = 1
        end = n
        middle = (start + end) // 2
        while start <= end:
            if isBadVersion(middle - 1):
                end = middle - 1
            else:
                start = middle + 1
            middle = (start + end) // 2
        return middle


def main():
    solution = Solution()
    ret = solution.firstBadVersion()
    print(ret)


if __name__ == '__main__':
    main()
