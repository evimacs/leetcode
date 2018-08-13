class Solution(object):
    def isPerfectSquare(self, num):
        """

        :type num: int
        :rtype: bool
        """
        start = 1
        end = num
        while start <= end:
            middle = (start + end) // 2
            pow_middle = middle * middle
            if pow_middle > num:
                end = middle - 1
            elif pow_middle < num:
                start = middle + 1
            else:
                return True
        return False

def main():
    solution = Solution()
    ret = solution.isPerfectSquare(100)
    print(ret)


if __name__ == '__main__':
    main()
