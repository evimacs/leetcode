class Solution(object):
    def countSegments(self, s):
        """

        :type s: str
        :rtype: int
        """

        flag = 0
        word = ''
        for x in s:
            if not x.isalpha():
                if not word:
                    flag += 1
                    word = ''
            else:
                word += x
        return flag


def main():
    solution = Solution()
    ret = solution.countSegments('Hello, my name is John')
    print(ret)


if __name__ == '__main__':
    main()
