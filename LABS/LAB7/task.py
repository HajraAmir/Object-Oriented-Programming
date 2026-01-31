class Tree:
    def __init__(self):
        self.root = None
        self.item = []  
        self.pred = []   
        self.parent_keys = []

    def addObject(self, key, value, parentKey):
        self.item.append(key)   
        self.pred.append(value)  
        self.parent_keys.append(parentKey)
        if parentKey == -1:
            self.root = key

    def printTreeAsArrays(self):
        combined_output = [f"({self.item[i]}, {self.pred[i]})" for i in range(len(self.item))]
        print("ITEM:", combined_output)
        print("PRED:", self.parent_keys)

    def searchParentKey(self, childKey):
        for i in range(len(self.item)):
            if self.item[i] == childKey:  
                return self.parent_keys[i]
        return None

    def printChildren(self, parentKey=None):
        if parentKey is None:
            parentKey = self.root

        parent_children = []
        for i in range(len(self.item)):
            if self.parent_keys[i] == parentKey:
                child, child_data = self.item[i], self.pred[i]  
                parent_children.append((child, child_data))

        print(f"Children of {parentKey}:", end=' ')
        for i in range(len(parent_children)):
            child, child_data = parent_children[i]
            print(f"({child}, {child_data})", end=' ' if i < len(parent_children) - 1 else '')
        print()

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