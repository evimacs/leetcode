class Solution(object):
    def reverseWords(self, s):
        """

        :type s: str
        :rtype: str
        """
        return ' '.join(map(lambda x: x[::-1], s.split()))


def main():
    solution = Solution()
    ret = solution.reverseWords("Let's take LeetCode contest")
    print(ret)


if __name__ == '__main__':
    main()
