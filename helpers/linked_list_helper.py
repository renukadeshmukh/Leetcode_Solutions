

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    @staticmethod
    def printLinkedList(head):
        cur = head
        while cur != None:
            print(cur.val, '-->>')
            cur = cur.next

    @staticmethod
    def array_to_linkedlist(nums):
        head = ListNode(nums[0])
        cur = head
        for n in nums[1:]:
            node = ListNode(n)
            cur.next = node
            cur = cur.next
        return head