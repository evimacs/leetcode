class ListNode(object):
    def __init__(self, x, node=None):
        self.val = x
        self.next = node


class Solution(object):
    def isPalindrome(self, head):
        """

        :type head: ListNode
        :rtype: bool
        """
        temp = list()
        while head:
            temp.append(head.val)
            head = head.next
        return temp == temp[::-1]


def main():
    solution = Solution()
    ret = solution.isPalindrome([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
