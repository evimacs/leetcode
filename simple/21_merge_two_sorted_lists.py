class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2

        if not l2:
            return l1

        pMergedHead = None

        if l1.val < l2.val:
            pMergedHead = l1
            pMergedHead.next = self.mergeTwoLists(l1.next, l2)
        else:
            pMergedHead = l2
            pMergedHead.next = self.mergeTwoLists(l2.next, l1)

        return pMergedHead


def main():
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    solution = Solution()
    l3 = solution.mergeTwoLists(l1, l2)

    while True:
        print(l3.val)
        l3 = l3.next
        if not l3.next:
            print(l3.val)
            break

if __name__ == '__main__':
    main()
