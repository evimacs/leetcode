class Solution(object):
    def findWords(self, words):
        """

        :type words: List[str]
        :rtype: List[str]
        """

        temp_a = set('asdfghjkl')
        temp_b = set('zxcvbnm')
        temp_c = set('qwertyuiop')
        ret = list()
        for word in words:
            temp = set(word.lower())
            if not (temp - temp_a) or not (temp - temp_b) or not (
                    temp - temp_c):
                ret.append(word)
        return ret


def main():
    solution = Solution()
    ret = solution.findWords(["Hello", "Alaska", "Dad", "Peace", "wer"])
    print(ret)


if __name__ == '__main__':
    main()
