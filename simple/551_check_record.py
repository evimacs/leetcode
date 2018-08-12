class Solution(object):
    def checkRecord(self, s):
        """

        :type s: str
        :rtype: bool
        """
        if s.count('A') > 1:
            return False

        flag = 0
        for x in s:
            if x == 'L':
                flag += 1
                if flag > 2:
                    return False
            else:
                flag = 0
        return True


def main():
    solution = Solution()
    ret = solution.checkRecord()
    print(ret)


if __name__ == '__main__':
    main()
