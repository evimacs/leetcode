class Solution(object):
    def generate(self, numRows):
        """
        : type numRows: int
        : rtype: List[int]
        """
        ret = list()
        for i in range(numRows):
            if i == 0:
                _ret = [1]
            elif i == 1:
                _ret = [1, 1]
            else:
                _ret = [1]
                for j in range(1, i):
                    _ret.append(ret[i-1][j] + ret[i-1][j-1])
                _ret.append(1)
            ret.append(_ret)
        return ret


def main():
    solution = Solution()
    ret = solution.generate(5)
    print(ret)


if __name__ == '__main__':
    main()