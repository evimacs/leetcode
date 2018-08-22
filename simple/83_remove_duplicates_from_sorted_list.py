class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """

        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        pre = None
        cur = head
        while cur != None:
            pre = cur
            cur = cur.next
            while cur != None and cur.val == pre.val:
                pre.next = cur.next
                cur = cur.next

        return head


def main():
    solution = Solution()
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(2))))
    ret = solution.deleteDuplicates(head)
    while True:
        if not ret:
            break
        print(ret.val)
        ret = ret.next


if __name__ == '__main__':
    main()
