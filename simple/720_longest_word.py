class Solution(object):
    def longestWord(self, words):
        """

        :type words: List[str]
        :rtype: str
        """
        words.sort()
        res = ''
        temp = set()
        for word in words:
            if len(word) == 1 or word[:-1] in temp:
                res = word if len(word) > len(res) else res
                temp.insert(word)
        return res


def main():
    solution = Solution()
    ret = solution.longestWord([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
