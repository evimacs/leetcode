class Solution(object):
    def reverseVowel(self, s):
        """

        :type s: str
        :rtype: str
        """
        s = list(s)
        vowel = 'aeiou'
        vowels = list()
        indexs = list()
        for x, y in enumerate(s):
            if y.lower() in vowel:
                vowels.append(y)
                indexs.append(x)
        print(vowels[::-1])
        for x, y in zip(indexs, vowels[::-1]):
            s[x] = y
        return ''.join(s)


def main():
    solution = Solution()
    ret = solution.reverseVowel('leetcode')
    print(ret)


if __name__ == '__main__':
    main()
