class Set:
    def _init_(self, sz):
        self.size = sz
        self.storage = [None] * self.size  # Simulate fixed-size array using list
        self.count = 0  # Track the actual number of elements in the set
        self.universal = []  # Universal set
    
    def add(self, i):
        if i not in self.storage:
            if self.count < self.size:
                self.storage[self.count] = i
                self.count += 1
    
    def remove(self, i):
        if i in self.storage:
            self.storage.remove(i)
            self.storage.append(None)
            self.count -= 1
    
    def _str_(self):
        return "{" + ", ".join([str(i) for i in self.storage if i is not None]) + "}"
    
    def _repr_(self):
        return self._str_()
    
    def union(self, other):
        result = Set(max(self.size, other.size))
        for item in self.storage + other.storage:
            if item is not None:
                result.add(item)
        return result
    
    def intersection(self, other):
        result = Set(min(self.size, other.size))
        for item in self.storage:
            if item in other.storage:
                result.add(item)
        return result
    
    def difference(self, other):
        result = Set(self.size)
        for item in self.storage:
            if item not in other.storage:
                result.add(item)
        return result
    
    def complement(self):
        result = Set(len(self.universal))
        for item in self.universal:
            if item not in self.storage:
                result.add(item)
        return result
    

    def get_universal(self):
        return self.universal
    
    def set_universal(self, universal_list):
        self.universal = universal_list


s1 = Set(10)
s2 = Set(10)
s1.set_universal([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s2.set_universal([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

s1.add(1)
s1.add(3)
s1.add(5)

s2.add(2)
s2.add(3)
s2.add(6)
s2.remove(6)
print("removal",s2)
print("S1:", s1)
print("S2:", s2)
print("Union:", s1.union(s2))
print("Intersection:", s1.intersection(s2))
print("Difference (S1 - S2):", s1.difference(s2))
print("Complement of S1:", s1.complement())