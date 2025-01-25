

class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = pow(2, depth + 1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        return self.FindKeyIndexRecursive(key, 0)

    def FindKeyIndexRecursive(self, key, index):
        if index > len(self.Tree):
            return None
        if self.Tree[index] is None:
            return -index
        if self.Tree[index] == key:
            return index
        if self.Tree[index] > key:
            return self.FindKeyIndexRecursive(key, 2 * index + 1)
        return self.FindKeyIndexRecursive(key, 2 * index + 2)

    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is None:
            return -1
        if index < 0 or index == 0:
            self.Tree[abs(index)] = key
        return abs(index)