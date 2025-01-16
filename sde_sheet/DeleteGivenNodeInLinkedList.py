class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        return node
    def print_list(self, head):
        while head:
            print(head.val)
            head = head.next
if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)

    s = Solution()
    removed_head = s.deleteNode(head.next)
    s.print_list(removed_head)  # Output: 4 1 9