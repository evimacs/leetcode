class Solution(object):
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            ret = 0
            a = x
            while True:
                _mod = x % 10
                ret = ret * 10 + _mod
                x = x // 10
                if abs(x) < 9:
                    ret = ret * 10 + x
                    break
            return ret == a


def main():
    solution = Solution()
    result = solution.isPalindrome(1724334271)
    print(result)


if __name__ == '__main__':
    main()