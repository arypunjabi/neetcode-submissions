class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        res = max(piles)
        while L <= R:
            mid = (L + R)//2
            runTotal = 0

            for n in piles:
                runTotal = runTotal + math.ceil(n/mid)
            if runTotal <= h:
                R = mid-1
                res = mid
            else:
                L = mid + 1
        return res
