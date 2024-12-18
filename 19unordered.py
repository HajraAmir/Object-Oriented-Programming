# array based version of linked nodes based code in doubly-LL5.py
class Unordered:
#    class Node: not required for array based list, delete this line

    def __init__(self, ARSize = 100):
        self.ARSize=ARSize
        self.ALSize=0
        self.Array=[None]*self.ARSize

    class UOIterator:
        def __init__(self, index=0, list=None):
            self.current = index-1
            self.list = list
        def __next__( self ):
            if self.current != self.list.ALSize-1:
                self.current = self.current + 1
                return self.list.Array[self.current]
            else:
                raise StopIteration

    def __iter__(self):
        return self.UOIterator(0, self)  # index 0 is the locations of FIRST object in array

    def isFull(self):
        return self.ALSize == self.ARSize

    def isEmpty(self):
        return self.ALSize == 0

    def size(self):
        return self.ALSize

    def append(self,o):
        if not self.isFull():
            self.Array[self.ALSize] = o
            self.ALSize = self.ALSize + 1

    def remove(self, index):
        if type(index) is self.UOIterator:
            index = index.current
        if index < 0 or index >= self.ALSize:
            raise Exception("Invalid Index")
        j = index
        while j < self.ALSize:
            self.Array[j] = self.Array[j+1]
            j = j + 1
        self.ALSize = self.ALSize - 1


    def set(self, index, o):
        pass
        # assign o at index in array
            
def main():
    # Create a new Doubly Linked List
    AL = Unordered()
    # Insert the element to empty list
    AL.append(10)
    # Insert the element at the end
    AL.append(20)
    AL.append(30)
    AL.append(70)
    AL.append(50)
    AL.append(60)
    AL.append(80)
    AL.append(90)
    AL.append(40)
    # Delete elements from start
    AL.remove(0)
    AL.remove(4)

    print("OUTPUT of 'for d in AL:'")
    for d in AL:
        print(d)
    print()

main()

