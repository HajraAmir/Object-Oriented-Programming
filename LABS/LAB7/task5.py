class Tree:
    def __init__(self):
        self.root = None
        self.item = []
        self.data = []
        self.parent_keys = []
    def addObject(self, key, value, parentKey):
        self.item.append((key, value))
        self.data.append(parentKey)
    def printTreeAsArrays(self):
        print("keys:", self.item)
        print("data:", self.data)
      
    def searchParentKey(self, childKey):
        for i in range(len(self.item)):
            if self.item[i] == childKey:
                return self.parent_keys[i]
        return None
    def printChildren(self, parentKey=None):
        if parentKey is None:
            parentKey = self.root
        parent_children = [self.item[i] for i in range(len(self.parent_keys)) if self.parent_keys[i] == parentKey]
        print(f"Children of {parentKey}:", parent_children)
    def countLeaves(self):
        return sum(1 for key in self.item if key not in self.parent_keys)
tree = Tree()
tree.addObject(20, 'H', -1)
tree.addObject(30, 'F', 20)
tree.addObject(70, 'U', 20)
tree.addObject(90, 'N', 30)
tree.addObject(60, 'Y', 70)
tree.addObject(10, 'B', 90)
tree.addObject(80, 'O', 70)
tree.addObject(40, 'X', 70)
tree.addObject(50, 'Z', 10)
tree.addObject(33, 'K', 90)
tree.printTreeAsArrays()
print("Parent of 30:", tree.searchParentKey(30))
tree.printChildren(20)  
print("Number of leaves:", tree.countLeaves())