class Solution(object):
    def isHappy(self, n):
        """

        :type n: int
        :rtype: bool
        """
        ret = list()
        now_sum = sum(list(map(lambda x: pow(int(x), 2), str(n))))
        ret.append(now_sum)
        while True:
            if now_sum == 1:
                return True
            now_sum = sum(list(map(lambda x: pow(int(x), 2), str(now_sum))))
            if now_sum in ret:
                return False
            ret.append(now_sum)


def main():
    solution = Solution()
    ret = solution.isHappy(19)
    print(ret)


if __name__ == '__main__':
    main()
