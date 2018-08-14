class Solution(object):
    def countPrimes(self, n):
        """

        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        _ret = 1
        if n == 3:
            return 1
        rets = [2]
        for x in range(3, n, 2):
            flag = 0
            for ret in rets[::-1]:
                if x % ret == 0:
                    flag = 1
                    break
            if not flag:
                rets.append(x)
                _ret += 1
        return _ret


def main():
    solution = Solution()
    ret = solution.countPrimes(10)
    print(ret)


if __name__ == '__main__':
    main()
