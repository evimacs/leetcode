class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for x in zip(*strs):
            if len(set(x)) == 1:
                res += x[0]
            else:
                break
        return res


def main():
    solution = Solution()
    result = solution.longestCommonPrefix(["flower", "flow", ""])
    print(result)


if __name__ == '__main__':
    main()
