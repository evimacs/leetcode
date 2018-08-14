class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """

        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        start = 0
        end = len(letters) - 1
        target = ord(target)

        while start <= end:
            middle = (start + end) // 2
            if ord(letters[middle]) > target:
                end = middle - 1
            elif ord(letters[middle]) <= target:
                start = middle + 1
        try:
            return letters[start]
        except Exception:
            return letters[0]


def main():
    solution = Solution()
    ret = solution.nextGreatestLetter()
    print(ret)


if __name__ == '__main__':
    main()
