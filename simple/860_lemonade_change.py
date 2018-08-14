class Solution(object):
    def lemonadeChange(self, bills):
        """

        :type bills: List[int]
        :rtype: bool
        """
        for i in bills:
            if i == 10:
                _i = bills.index(5)
                if bills.index(i) < _i or _i == -1:
                    return False
                else:
                    bills[_i] = 0
                    bills[bills.index(i)] = 5
            else:
                _i = bills.index(5)
                if bills.index(i) < _i or _i == -1:
                    return False
                _i = bills.index(10)
                if bills.index(i) < _i or _i == -1:
                    return False
                else:
                    bills[_i] = 0
                    bills[bills.index(i)] = 5
        return True


def main():
    solution = Solution()
    ret = solution.lemonadeChange([5, 5, 10, 10, 20])
    print(ret)


if __name__ == '__main__':
    main()
