from typing import List


class SegmentTree:

    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.segment = [0] * self.size + nums
        for i in range(self.size - 1, 0, -1):
            self.segment[i] = self.segment[2 * i] + self.segment[2 * i + 1]

    def update(self, i: int, val: int) -> None:
        i += self.size
        diff = val - self.segment[i]
        while i > 0:
            self.segment[i] += diff
            i //= 2

    def sumRange(self, i: int, j: int) -> int:
        i += self.size
        j += self.size
        res = 0
        while i <= j:
            if i % 2:
                res += self.segment[i]
                i += 1
            if j % 2 == 0:
                res += self.segment[j]
                j -= 1
            i //= 2
            j //= 2
        return res

    def updateRange(self, i: int, j: int, diff: int) -> None:
        factor = 1
        width = j - i + 1
        head, tail = 1, 1
        while i != j:
            self.segment[i] += head * diff
            self.segment[j] += tail * diff
            for k in range(i + 1, j):
                self.segment[k] += factor * diff
            i, r1 = divmod(i, 2)
            j, r2 = divmod(j, 2)
            if r1 == 0:
                head += factor
            if r2 != 0:
                tail += factor
            factor *= 2
        diff *= width
        while i:
            self.segment[i] += diff
            i //= 2
