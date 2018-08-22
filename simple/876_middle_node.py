class ListNode(object):
    def __init__(self, x, node=None):
        self.val = x
        self.next = node


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        flag = 0
        p = head
        while p:
            flag += 1
            p = p.next
        a = 0
        while head:
            a += 1
            if a == flag // 2 + 1:
                return head
            head = head.next
        return head


def main():
    solution = Solution()
    ret = solution.middleNode([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
