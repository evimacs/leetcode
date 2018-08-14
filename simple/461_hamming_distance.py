class Solution(object):
    def hammingDistance(self, x, y):
        """

        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:]
        y = bin(y)[2:]
        ret = 0
        if len(x) > len(y):
            y = '0' * (len(x) - len(y)) + y
        else:
            x = '0' * (len(y) - len(x)) + x
        for i in range(len(x)):
            if x[i] != y[i]:
                ret += 1
        return ret


def main():
    solution = Solution()
    ret = solution.hammingDistance()
    print(ret)


if __name__ == '__main__':
    main()
