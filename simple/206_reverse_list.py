class ListNode(object):
    def __init__(self, x, node=None):
        self.val = x
        self.next = node


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head
        new_cur = None
        while cur:
            temp = cur.next
            cur.next = new_cur
            new_cur = cur
            cur = temp
        return new_cur


def main():
    solution = Solution()
    ret = solution.reverseList([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
