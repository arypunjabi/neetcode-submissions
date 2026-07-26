class HeapQueueDistance:
    def __init__(self):
        self.heap = [0]
    
    def calcDistance(self, point):
        return (point[0]**2 + point[1]**2)**0.5

    def push(self, point):
        distance = self.calcDistance(point)
        self.heap.append([point,distance])
        i = len(self.heap)-1
        
        while i > 1 and self.heap[i][1] < self.heap[i//2][1]:
            tmp = self.heap[i//2]
            self.heap[i//2] = self.heap[i]
            self.heap[i] = tmp

            i = i//2
    
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()[0]
        
        returnVal = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1

        while i * 2 < len(self.heap):
            if ((i * 2) + 1) < len(self.heap) and self.heap[i * 2 + 1][1] < self.heap[i * 2][1] and self.heap[i][1] > self.heap[i * 2 + 1][1]:
                #swap right
                tmp = self.heap[i * 2 + 1]
                self.heap[i*2+1] = self.heap[i]
                self.heap[i] = tmp

                i = i * 2 + 1
            elif self.heap[i][1] > self.heap[i * 2][1]:
                #swap left
                tmp = self.heap[i * 2]
                self.heap[i*2] = self.heap[i]
                self.heap[i] = tmp

                i = i * 2
            else:
                break
        return returnVal[0]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distanceHeap = HeapQueueDistance()
        returnList = []

        for point in points:
            distanceHeap.push(point)
        for i in range(k):
            returnList.append(distanceHeap.pop())
        
        return returnList

            