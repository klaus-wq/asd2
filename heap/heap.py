class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        maxSize = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * maxSize
        for key in a:
            self.Add(key)

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        if self.HeapArray.count(None) == len(self.HeapArray):
            return -1  # если куча пуста

        maxKey = self.HeapArray[0]
        self.HeapArray[0] = None

        index = len(self.HeapArray) - 1
        lastEmptyIndex = None
        while index >= 0 and self.HeapArray[index] is None:
            index -= 1
        if index >= 0:
            lastEmptyIndex = index

        if lastEmptyIndex is not None:
            self.HeapArray[0] = self.HeapArray[lastEmptyIndex]
            self.HeapArray[lastEmptyIndex] = None
            self.shiftDown(0)

        return maxKey

    def shiftDown(self, currentIndex):
        maxIndex = currentIndex
        leftChildIndex = 2 * currentIndex + 1
        rightChildIndex = 2 * currentIndex + 2

        if (leftChildIndex < len(self.HeapArray) and self.HeapArray[leftChildIndex] is not None
                and self.HeapArray[leftChildIndex] > self.HeapArray[maxIndex]):
            maxIndex = leftChildIndex
        if (rightChildIndex < len(self.HeapArray) and self.HeapArray[rightChildIndex] is not None
                and self.HeapArray[rightChildIndex] > self.HeapArray[maxIndex]):
            maxIndex = rightChildIndex

        if maxIndex == currentIndex:
            return None

        self.HeapArray[currentIndex], self.HeapArray[maxIndex] = self.HeapArray[maxIndex], self.HeapArray[currentIndex]
        self.shiftDown(maxIndex)

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        if self.HeapArray.count(None) == 0:
            return False  # если куча вся заполнена

        index = 0
        lastNotEmptyIndex = None
        while index < len(self.HeapArray) and self.HeapArray[index] is not None:
            index += 1
        if index < len(self.HeapArray):
            lastNotEmptyIndex = index

        if lastNotEmptyIndex is not None:
            self.HeapArray[lastNotEmptyIndex] = key
            self.shiftUp(lastNotEmptyIndex)

        return True

    def shiftUp(self, currentIndex):
        parent = (currentIndex - 1) // 2
        if (currentIndex > 0 and self.HeapArray[currentIndex] is not None
                and self.HeapArray[currentIndex] > self.HeapArray[parent]):
            self.HeapArray[currentIndex], self.HeapArray[parent] = self.HeapArray[parent], self.HeapArray[currentIndex]
            self.shiftUp(parent)