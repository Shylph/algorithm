queue = []
queue.insert(0,"data")
data = queue.pop()
# -----------------
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.insert(0, val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0


# --------------------------
from collections import deque

fifi = deque()
fifi.append(1)
x = fifi.popleft()


# ----------------------
import heapq

a = []
heapq.heappush(a, 5)
heapq.heappush(a, 3)
heapq.heappush(a, 7)
heapq.heappush(a, 4)

# 힙의 0 인덱스에 접근하면 항상 가장 작은 아이템을 반환
# a[0] == heapq.nsmallest(1,a)[0]  # 같음

