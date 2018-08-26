class Solution(object):
    def isAnagram(self, s, k):
        """

        :type s: str
        :type k: str
        :rtype: bool
        """
        temp_1 = set(s)
        temp_2 = set(k)
        if temp_1 != temp_2:
            return False
        for x in temp_1:
            if s.count(x) != k.count(x):
                return False
        return True


def main():
    solution = Solution()
    ret = solution.isAnagram()
    print(ret)


if __name__ == '__main__':
    main()
