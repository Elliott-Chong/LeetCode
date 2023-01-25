class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode()
    cursor = result
    carry = 0
    while l1 or l2 or carry:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        curr_val = l1_val + l2_val + carry
        carry = curr_val // 10
        curr_val %= 10
        cursor.next = ListNode(curr_val)
        cursor = cursor.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return result.next
