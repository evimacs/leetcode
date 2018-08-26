class ListNode(object):
    def __init__(self, x, node=None):
        self.val = x
        self.next = node


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """

        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while (p1 != p2):
            p1 = headB if p1 == None else p1.next
            p2 = headA if p2 == None else p2.next
        return p1


def main():
    solution = Solution()
    ret = solution.getIntersectionNode([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
