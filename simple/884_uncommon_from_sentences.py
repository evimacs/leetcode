class Solution(object):
    def uncommonFromSentences(self, A, B):
        """

        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a = A.split()
        b = B.split()
        temp = set(a).union(set(b))
        a.extend(b)
        ret = list()
        for word in temp:
            if a.count(word) == 1:
                ret.append(word)
        return ret


def main():
    solution = Solution()
    ret = solution.uncommonFromSentences('this apple is sweet',
                                         'this apple is sour')
    print(ret)


if __name__ == '__main__':
    main()
