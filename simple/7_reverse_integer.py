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
            if x < 10:
                return x
            _mod = x % 10
            ret = ret * 10 + _mod
            x = x // 10
            if abs(x) <= 9:
                ret = ret * 10 + x
                ret = ret * flag
                if ret < -1 * pow(2, 31) or ret > pow(2, 31) - 1:
                    ret = 0
                return ret


def main():
    solution = Solution()
    result = solution.reverse(-173)
    print(result)


if __name__ == '__main__':
    main()
