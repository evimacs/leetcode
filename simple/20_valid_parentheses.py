class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses_dict = {'[': ']', '(': ')', '{': '}'}
        push_str = '{[('
        push_list = list()
        for x in s:
            if x in push_str:
                push_list.append(x)
            else:
                y = push_list.pop() if push_list else ''
                parentheses = parentheses_dict.get(y)
                if not parentheses or x != parentheses:
                    return False
        return True


def main():
    solution = Solution()
    result = solution.isValid(']')
    print(result)


if __name__ == '__main__':
    main()
