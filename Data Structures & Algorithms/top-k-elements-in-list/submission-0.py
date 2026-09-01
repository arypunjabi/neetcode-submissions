class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        myHash = {}
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            if i in myHash:
                myHash[i] += 1
            else:
                myHash[i] = 1

        for num, count in myHash.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res