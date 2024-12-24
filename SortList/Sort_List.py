class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        no1, no2 = head, head.next
        while no2 and no2.next:
            no1 = no1.next
            no2 = no2.next.next
        segunda_metade = no1.next
        no1.next = None

        left = self.sortList(head)
        right = self.sortList(segunda_metade)

        return self.mergeSortedLists(left, right)

    def mergeSortedLists(self, l1, l2):
        temp = ListNode(-1)
        current = temp

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2

        return temp.next