class EmptyHeapError(Exception):
    def __init__(self, method: str, message="Min Heap is empty."):
        self.method = method 
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"MinHeap.{self.method}: {self.message}"

class MinHeap:
    def __init__(self, array = None):
        self.items = [] if array is None else array
        self.size = 0

    def __str__(self):
        return f"{self.items}"

    def _getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1

    def _getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2

    def _getParentIndex(self, childIndex: int):
        # [0,1,2,3,4,5,6] - 1 and 2 have child nodes
        # 3 and 4's parent is 1, 5 and 6's parent is 2
        return (childIndex - 1) // 2

    def _hasLeftChild(self, index: int):
        return self._getLeftChildIndex(index) < self.size

    def _hasRightChild(self, index: int):
        return self._getRightChildIndex(index) < self.size

    def _hasParent(self, index: int):
        # Only scenario where a value would not have a parent is the root element.
        return self._getParentIndex(index) >= 0

    def _leftChildValue(self, index: int):
        return self.items[self._getLeftChildIndex(index)]

    def _rightChildValue(self, index: int):
        return self.items[self._getRightChildIndex(index)]

    def _parentValue(self, index: int):
        return self.items[self._getParentIndex(index)]

    def peek(self):
        if (self.size == 0):
            raise EmptyHeapError("peek")

        return self.items[0]

    def poll(self):
        if (self.size == 0):
            raise EmptyHeapError("peek")

        min_item = self.items[0]
        self.items[0] = self.items.pop()
        self.heapifyDown()
        return min_item

    def _swap(self, indexOne:int, indexTwo:int):
        temp = self.items[indexOne]
        self.items[indexOne] = self.items[indexTwo]
        self.items[indexTwo] = temp

    def add(self, value: int):
        self.items.append(value)
        self.size+=1
        self.heapifyUp()

    # Swaps the most recently added element in the heap to its appropriate position in the list
    def heapifyUp(self):
        index = self.size - 1
        print(index)

        while self._hasParent(index) and self._parentValue(index) > self.items[index]:
            # swap elements and update the index so we can move up the heap and compare again
            self._swap(index, self._getParentIndex(index))
            index = self._getParentIndex(index)

    def heapifyDown(self):
        index = 0

        while self._hasLeftChild(index):
            smallerChildIndex = self._getLeftChildIndex(index)

            # Check if there is a right child and see if the right child is smaller than the left child
            if self._hasRightChild(index) and (self._rightChildValue(index) < self._leftChildValue(index)):
                smallerChildIndex = self._getRightChildIndex(index)

            if self.items[index] < self.items[smallerChildIndex]:
                break
            else:
                self._swap(index, smallerChildIndex)
            
            index = smallerChildIndex


    # TODO: add method to get heapify the entire heap




def main():
    # TODO: given min heap, turn it into max heap
    heap = MinHeap()
    heap.add(5)
    heap.add(28)
    heap.add(1)
    heap.add(8)
    heap.add(2)
    heap.add(8)

    print("peek:", heap.peek())
    print("heap size:", heap.size)
    print("heap:", str(heap))


if __name__ == "__main__":
    main()
