class Solution(object):
    def toGoatLatin(self, S):
        """

        :type S: str
        :rtype: str
        """
        temp = 'aeiouAEIOU'
        s = S.split()
        ret = list()
        for y, x in enumerate(s, 1):
            if x[0] in temp:
                x = x + 'ma'
            else:
                x = x[1::] + x[0] + 'ma'
            x += 'a' * y
            ret.append(x)
        return ' '.join(ret)


def main():
    solution = Solution()
    ret = solution.toGoatLatin('I speak Goat Latin')
    print(ret)


if __name__ == '__main__':
    main()
