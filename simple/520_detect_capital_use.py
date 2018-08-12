class Solution(object):
    def detectCapitalUse(self, word):
        """

        :type word: str
        :rtype: bool
        """
        return (word.upper() == word) or (word.lower() == word) or (
                word.capitalize() == word)


def main():
    solution = Solution()
    ret = solution.detectCapitalUse()
    print(ret)


if __name__ == '__main__':
    main()
