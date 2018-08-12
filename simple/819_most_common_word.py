class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """

        :type paragraph: str
        :type banned: list[str]
        :rtype: str
        """
        word_count = {}
        word = ''
        for x in paragraph:
            if x.isalnum():
                word += x.lower()
            else:
                if word not in banned and word:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
                word = ''
        if word and word not in banned:
            word_count.setdefault(word, 0) + 1
        if word_count:
            return \
            list(sorted(word_count.items(), key=lambda x: x[1], reverse=True))[
                0][0]
        else:
            return ''


def main():
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    solution = Solution()
    ret = solution.mostCommonWord(paragraph, banned)
    print(ret)


if __name__ == '__main__':
    main()
