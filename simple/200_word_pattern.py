class Solution(object):
    def wordPattern(self, pattern, str):
        """

        :type pattern: str
        :type str: str
        :rtype: bool
        """
        temp_dict = dict()
        if len(pattern) != len(str.split(' ')):
            return False
        if len(set(pattern)) == len(pattern) and len(str.split(' ')) == len(set(str.split(' '))):
            return True

        for x, y in zip(list(pattern), str.split(' ')):
            if x in temp_dict:
                if y != temp_dict.get(x):
                    return False
            else:
                temp_dict[x] = y

            if y in temp_dict:
                if x != temp_dict.get(y):
                    return False
            else:
                temp_dict[y] = x
        return True


def main():
    solution = Solution()
    ret = solution.wordPattern('abba', 'dog cat cat dog')
    print(ret)
    pattern = "abba"
    str = "dog cat cat fish"
    ret = solution.wordPattern(pattern, str)
    print(ret)
    pattern = "aaaa"
    str = "dog cat cat dog"
    ret = solution.wordPattern(pattern, str)
    print(ret)
    pattern = "abba"
    str = "dog dog dog dog"
    ret = solution.wordPattern(pattern, str)
    print(ret)

if __name__ == '__main__':
    main()
