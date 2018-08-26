class Solution(object):
    def lemonadeChange(self, bills):
        """

        :type bills: List[int]
        :rtype: bool
        """
        temp_5 = list()
        temp_10 = list()
        for bill in bills:
            if bill == 5:
                temp_5.append(5)
            elif bill == 10:
                try:
                    temp_10.append(10)
                    del temp_5[-1]
                except Exception:
                    return False
            else:
                try:
                    del temp_5[-1]
                except Exception:
                    return False
                if temp_10:
                    del temp_10[-1]
                else:
                    try:
                        del temp_5[-1]
                        del temp_5[-1]
                    except Exception:
                        return False
        return True


def main():
    solution = Solution()
    ret = solution.lemonadeChange([5, 5, 10, 10, 20])
    print(ret)


if __name__ == '__main__':
    main()
