class Set:
    def __init__(self):
        self.items = []

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def union(self, other):
        union_set = Set()
        union_set.items = self.items.copy()
        for item in other.items:
            if item not in union_set.items:
                union_set.items.append(item)
        return union_set

    def intersection(self, other):
        intersection_set = Set()
        for item in self.items:
            if item in other.items:
                intersection_set.items.append(item)
        return intersection_set

    def difference(self, other):
        difference_set = Set()
        difference_set.items = self.items.copy()
        for item in other.items:
            if item in difference_set.items:
                difference_set.items.remove(item)
        return difference_set


set1 = Set()
set1.add(1)
set1.add(2)
set1.add(3)

set2 = Set()
set2.add(3)
set2.add(4)
set2.add(5)

print("Set 1:", set1.items)
print("Set 2:", set2.items)
print("Union:", set1.union(set2).items)
print("Intersection:", set1.intersection(set2).items)
print("Difference:", set1.difference(set2).items)