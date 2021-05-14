# Problem Statement
# https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
# https://leetcode.com/problems/merge-k-sorted-lists/

from queue import PriorityQueue
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        p_queue = PriorityQueue()
        prev_node = None
        new_head = None

        for ll in lists:
            if ll:
                p_queue.put((ll.val, ll))

        while p_queue:
            val, node = p_queue.get()
            if prev_node:
                prev_node.next = node
            else:
                prev_node = node
                new_head = prev_node

            next_node = node.next

            if next_node:
                p_queue.put((next_node.val, next_node))

        prev_node.next = None

        return new_head



