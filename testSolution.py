from typing import List, Optional
from util.listNode import ListNode


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        ints = [[[None] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        self.m = m
        self.n = n
        self.mod = 10 ** 9 + 7
        return self.helper(maxMove, startRow, startColumn, ints)

    def helper(self, maxMove, startRow, startColumn, ints):
        if startRow < 0 or startRow >= self.m or startColumn < 0 or startColumn >= self.n:
            return 1
        if maxMove <= 0:
            return 0
        if ints[startRow][startColumn][maxMove] is not None:
            return ints[startRow][startColumn][maxMove]
        tempCount = 0

        tempCount = (tempCount + self.helper(maxMove - 1, startRow + 1, startColumn, ints)) % self.mod
        tempCount = (tempCount + self.helper(maxMove - 1, startRow, startColumn - 1, ints)) % self.mod
        tempCount = (tempCount + self.helper(maxMove - 1, startRow - 1, startColumn, ints)) % self.mod
        tempCount = (tempCount + self.helper(maxMove - 1, startRow, startColumn + 1, ints)) % self.mod

        ints[startRow][startColumn][maxMove] = tempCount
        return tempCount


def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    sum = 0
    current = head
    while current:
        sum += current.val
        if sum == 0:
            return removeZeroSumSublists(1,current.next)
        current = current.next
    head.next = removeZeroSumSublists(1,head.next)
    return head
    # Your runtime beats 36.64 % of Python3 submissions
    # Your memory usage beats 37.09 % of Python3 submissions (41.70 MB)


def minimumLength(self, s: str) -> int:
    start, end = 0, len(s)
    while start < end and s[start] == s[end]:
        charS = s[start]
        while start <= end and charS == s[start]:
            start += 1
        while start <= end and charS == s[end]:
            end -= 1
    return end + 1 - start
