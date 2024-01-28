class stack:
    def __init__(self):
        self.s = []
    def empty(self):
        return self.s == []
    def pop(self):
        return self.s.pop()
    def push(self, start):
        self.s.append(start)
    def size(self):
        return len(self.s)
class queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def empty(self):
        return self.q == []
    def enqueue(self, start):
        self.s1.insert(0,start)
    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
q = queue()
q.enqueue(5)
q.enqueue(1)
q.enqueue(4)
print(q.dequeue())