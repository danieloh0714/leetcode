from queue import PriorityQueue


class MedianFinder:

    def __init__(self) -> None:
        self.lower = PriorityQueue() # max heap
        self.upper = PriorityQueue() # min heap

    def add_num(self, num: int) -> None:
        self.lower.put(-num)

        if not self.upper.empty() and -self.lower.queue[0] > self.upper.queue[0]:
            self.upper.put(-self.lower.get())

        if self.lower.qsize() > self.upper.qsize()+1:
            self.upper.put(-self.lower.get())
        elif self.upper.qsize() > self.lower.qsize()+1:
            self.lower.put(-self.upper.get())

    def find_median(self) -> float:
        if self.lower.qsize() > self.upper.qsize():
            return -self.lower.queue[0]
        if self.upper.qsize() > self.lower.qsize():
            return self.upper.queue[0]

        return (-self.lower.queue[0]+self.upper.queue[0])/2
