class Solution(object):
    def largeGroupPositions(self, S):
        """

        :type S: str
        :rtype: List[int]
        """
        return_list = []
        i, j, n = 0, 0, len(S)
        while i < n - 1:
            while i < n - 1 and S[i + 1] == S[i]:
                i += 1
            if i - j >= 2:
                return_list.append([j, i])
            i = i + 1;
            j = i
        return return_list


def main():
    solution = Solution()
    ret = solution.largeGroupPositions("abbxxxxzzy")
    print(ret)
    ret = solution.largeGroupPositions("aaa")
    print(ret)
    ret = solution.largeGroupPositions("abcdddeeeeaabbbcd")
    print(ret)


if __name__ == '__main__':
    main()
