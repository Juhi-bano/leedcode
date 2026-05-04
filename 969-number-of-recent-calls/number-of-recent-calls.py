class RecentCounter:
    def __init__(self):
        self.nq = []
        

    def ping(self, t: int) -> int:
        self.nq.append(t)
        while (t - self.nq[0]>3000):
            self.nq.pop(0)
        return len(self.nq)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)