"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        head = Node(node.val)
        nodeQueue = deque()
        nodeQueue.append(node)
        copy = {}
        copy[node] = head
        visit = set()
        visit.add(node)

        while nodeQueue:
            oldNode = nodeQueue.popleft()
            newNode = copy[oldNode]
            for tempNode in oldNode.neighbors:
                if tempNode in copy:
                    newNode.neighbors.append(copy[tempNode])
                else:
                    copy[tempNode] = Node(tempNode.val)
                    newNode.neighbors.append(copy[tempNode])
                if not(tempNode in visit):
                    nodeQueue.append(tempNode)
                    visit.add(tempNode)
        return head
                



