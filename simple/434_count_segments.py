class Solution(object):
    def countSegments(self, s):
        """

        :type s: str
        :rtype: int
        """

        return len(s.split())


def main():
    solution = Solution()
    ret = solution.countSegments('Hello, my name is John')
    print(ret)


if __name__ == '__main__':
    main()

