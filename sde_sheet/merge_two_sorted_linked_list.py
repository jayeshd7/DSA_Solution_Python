from sde_sheet.middle_node import ListNode


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class MergeTwoSortedLinkedList:
    def merge_two_sorted_linked_list(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        if head1.data <= head2.data:
            head1.next = self.merge_two_sorted_linked_list(head1.next, head2)
            return head1
        else:
            head2.next = self.merge_two_sorted_linked_list(head1, head2.next)
            return head2

    def print_list(self, head):
        while head:
            print(head.data)
            head = head.next

if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(4)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    m = MergeTwoSortedLinkedList()
    merged_head = m.merge_two_sorted_linked_list(head1, head2)
    m.print_list(merged_head)