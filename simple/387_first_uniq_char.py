class Solution(object):
    def firstUniqChar(self, s):
        """

        :type s:str
        :rtype: int
        """
        rets = list()
        for x in range(97, 123):
            temp = chr(x)
            if s.count(temp) == 1:
                rets.append(s.index(temp))
        return -1 if not rets else min(rets)



def main():
    solution = Solution()
    ret = solution.firstUniqChar([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
