class Tree:
    def __init__(self):
        self.item = []
        self.pred = []
        self.keys = []
        self.parent_keys = []
    def addObject(self, key, value, parentKey):
        self.item.append((key, value))
        self.pred.append(parentKey)

    def printTreeAsArrays(self):
        print("item:", self.item)
        print("pred:", self.pred)

    def searchParentKey(self, childKey):
        for i in range(len(self.item)):
            if self.item[i][0] == childKey:
               return self.pred[i]
        return None

    def printChildren(self, parentKey):
        children = []
        for i in range(len(self.item)):
            if self.pred[i] == parentKey:
              children.append(self.item[i][1])
        print("Children of", parentKey, ":", children)

    def countLeaves(self):
        return sum(1 for key in self.keys if key not in self.parent_keys)
def main():
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
    tree.printChildren(70)
    print("Number of leaves:", tree.countLeaves())

main()















