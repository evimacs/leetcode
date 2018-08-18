class Solution(object):
    def isOneBitCharacter(self, bits):
        """

        :type bits: List[int]
        :rtype: bool
        """
        i, n = 0, len(bits)
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == n - 1


def main():
    solution = Solution()
    ret = solution.isOneBitCharacter()
    print(ret)


if __name__ == '__main__':
    main()
