class Solution(object):
    def rotateDigits(self, n, ):
        """

        :type n: int
        :rtype: int
        """
        rotate_map = {'0': '0', '1': '1', '8': '8', '2': '5', '5': '2',
                      '6': '9', '9': '6'}
        flag = 0
        int_list = list()
        for x in range(1, n + 1):
            n1 = ''
            temp = str(x)
            for _temp in temp:
                n1 += rotate_map.get(_temp, 'a')
            try:
                flag += 1 if int(n1) != x else 0
                int_list.append(int(n1))
            except Exception:
                pass
        return flag


def main():
    solution = Solution()
    ret = solution.rotateDigits(857)
    print(ret)


if __name__ == '__main__':
    main()
