class ListNode(object):
    def __init__(self, x, node=None):
        self.val = x
        self.next = node


class Solution(object):
    def removeElements(self, head, val):
        """

        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr = head
        prev = head

        while curr is not None:
            if head.val == val:
                head = head.next
            elif curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return head

def main():
    solution = Solution()
    ret = solution.removeElements([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
