class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        print(self.arr[i])
    
    def set(self, i: int, n: int) -> None:
        pass

    def pushback(self, n: int) -> None:
        pass

    def popback(self) -> int:
        pass

    def resize(self) -> None:
        pass

    def getSize(self) -> int:
        pass
    
    def getCapacity(self) -> int:
        pass

DynamicArray(5)
DynamicArray.get()