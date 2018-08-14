class Solution(object):
    def selfDividingNumbers(self, left, right):
        """

        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = list()
        for i in range(left, right + 1):
            temp = str(i)
            if '0' in temp:
                continue
            flag = 0
            for x in set(temp):
                if i % int(x) != 0:
                    flag = 1
            if not flag:
                ret.append(i)
        return ret


def main():
    solution = Solution()
    ret = solution.selfDividingNumbers(1, 22)
    print(ret)


if __name__ == '__main__':
    main()
