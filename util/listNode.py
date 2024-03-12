from typing import List, Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createlistNode(self, arr: List[int]) -> Optional[ListNode]:
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    current = head
    for val in range(1, len(arr)):
        current.next = ListNode(arr[val])
        current = current.next
    return head


def printlistnode(self, node: ListNode) -> None:
    current = node
    while current:
        print(f"{current.val} -> ", end="")
        current = current.next
    print("Null")
