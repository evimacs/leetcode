class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        flag = -1 if x < 0 else 1
        x = x * flag
        while True:
            _mod = x % 10
            ret = ret * 10 + _mod
            x = x // 10
            if abs(x) < 9:
                ret = ret * 10 + x
                return ret * flag


def main():
    solution = Solution()
    result = solution.reverse(-173)
    print(result)


if __name__ == '__main__':
    main()
