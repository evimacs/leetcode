class Solution(object):
    def compress(self, chars):
        """

        :type chars: List[str]
        :rtype: int
        """

        temp_index = 0
        temp = ''
        temp_count = 0
        for i in range(len(chars)):
            if temp != chars[i]:
                temp = chars[i]

            else:
                chars[temp_index] += 1




def main():
    solution = Solution()
    ret = solution.compress(["a", "a", "b", "b", "c", "c", "c"])
    print(ret)


if __name__ == '__main__':
    main()

