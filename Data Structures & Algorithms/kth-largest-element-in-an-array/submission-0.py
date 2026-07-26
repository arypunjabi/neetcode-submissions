import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        for i in range(k):
            returnVal = heapq.heappop(maxHeap)
        return returnVal * -1