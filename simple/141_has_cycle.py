class Solution(object):
    def hasCycle(self, head):
        """

        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


def main():
    solution = Solution()
    ret = solution.hasCycle([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
