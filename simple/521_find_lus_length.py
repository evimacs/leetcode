class Solution(object):
    def findLUSlength(self, a, b):
        """

        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        else:
            return max(len(a), len(b))




def main():
    solution = Solution()
    ret = solution.findLUSlength([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
