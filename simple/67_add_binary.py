class Solution(object):
    def addBinary(self, a, b):
        """

        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


def main():
    solution = Solution()
    a = '11'
    b = '1'

    ret = solution.addBinary(a, b)
    print(ret)


if __name__ == '__main__':
    main()

