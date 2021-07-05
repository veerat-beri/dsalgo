from linkedlists import BuildSinglyLinkedList, SinglyLinkedList

l1 = BuildSinglyLinkedList([3, 7]).get_ll()
l2 = BuildSinglyLinkedList([9, 2]).get_ll()


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = first_node = SinglyLinkedList.get_new_node(None)
        pre_val = 0
        while l1 and l2:

            # print(l1.data, l2.data)
            # breakpoint()
            val_sum = l1.data + l2.data + pre_val
            remainder = val_sum % 10
            quotient = val_sum // 10
            # breakpoint()
            print(val_sum, remainder, quotient, pre_val)

            l3.next = SinglyLinkedList.get_new_node(remainder)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
            pre_val = quotient

        # print(l3.data, pre_val, l1, l2, sep="\n")

        while l1:
            val_sum = l1.data + pre_val
            remainder = val_sum % 10
            quotient = val_sum // 10

            l3.next = SinglyLinkedList.get_new_node(remainder)
            l1 = l1.next
            l3 = l3.next
            pre_val = quotient

        while l2:
            val_sum = l2.data + pre_val
            remainder = val_sum % 10
            quotient = val_sum // 10

            l3.next = SinglyLinkedList.get_new_node(remainder)
            l2 = l2.next
            l3 = l3.next
            pre_val = quotient

        if pre_val:
            l3.next = SinglyLinkedList.get_new_node(pre_val)

        return first_node.next

l3 = Solution().addTwoNumbers(l1.head, l2.head)
while l3:
    print(l3.data)
    l3 = l3.next

print()





