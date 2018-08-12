class Solution(object):
    def judgeCircle(self, moves):
        """

        :type moves: str
        :rtype: bool
        """
        if moves.count('R') == moves.count('L') and moves.count(
                'U') == moves.count('D'):
            return True
        return False


def main():
    solution = Solution()
    ret = solution.judgeCircle()
    print(ret)


if __name__ == '__main__':
    main()
