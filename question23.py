# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mini_heap = []

        for idx, no in enumerate(lists):
            if no:
                heapq.heappush(mini_heap, (no.val, idx, no))

        lista_nova = ListNode(-1)
        atual = lista_nova

        while mini_heap:
            val, idx, node = heapq.heappop(mini_heap)
            atual.next = node
            atual = atual.next
            if node.next:
                heapq.heappush(mini_heap, (node.next.val, idx, node.next))

        return lista_nova.next
