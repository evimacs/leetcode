class Solution(object):
    def islandPerimeter(self, grid):
        """

        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 1 and len(grid[0]) == 1:
            return 4
        return len(grid) * len(grid[0])


def main():
    solution = Solution()
    ret = solution.islandPerimeter()
    print(ret)


if __name__ == '__main__':
    main()
