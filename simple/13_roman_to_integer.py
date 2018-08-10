class Solution(object):
    def romanToInt(self, s):
        """
        :rtype s:str
        :rtype: int
        """
        roman_num_dict = {'I': 1, "V": 5, "X": 10,
                          "L": 50, "C": 100, "D": 500, "M": 1000}
        roman_len = len(s)
        res = 0

        for i in range(roman_len-1, -1, -1):
            if i != roman_len - 1:
                roman_i = roman_num_dict[s[i]]
                roman_i_1 = roman_num_dict[s[i + 1]]
                if roman_i < roman_i_1:
                    res -= roman_i
                else:
                    res += roman_i
            else:
                res += roman_num_dict[s[i]]
        return res


def main():
    solution = Solution()
    result = solution.romanToInt('MCMXCIV')
    print(result)


if __name__ == '__main__':
    main()
