class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                return None
        return None

    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        if v >= 0 and v < self.max_vertex and self.vertex[v] is not None:
            self.vertex[v] = None
            for i in range(self.max_vertex):
                self.m_adjacency[v][i] = 0
                self.m_adjacency[i][v] = 0
        return None

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if v1 < self.max_vertex and v2 < self.max_vertex and v1 >= 0 and v2 >= 0 and self.m_adjacency[v1][v2] == 1:
            return True
        return False

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        if v1 < self.max_vertex and v2 < self.max_vertex and v1 >= 0 and v2 >= 0:
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
        return None

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if v1 < self.max_vertex and v2 < self.max_vertex and v1 >= 0 and v2 >= 0:
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0
        return None

    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        if self.vertex[VFrom] is None or self.vertex[VTo] is None:
            return []
        for v in self.vertex:
            if v is not None:
                v.Hit = False
        path = Stack()
        return self.DepthFirstSearchRecursive(VFrom, VTo, path).stack

    def DepthFirstSearchRecursive(self, VFrom, VTo, path):
        self.vertex[VFrom].Hit = True
        path.push(self.vertex[VFrom])
        if self.m_adjacency[VFrom][VTo] == 1:
            path.push(self.vertex[VTo])
            return path
        for i in range(self.max_vertex):
            if self.m_adjacency[VFrom][i] == 1 and not self.vertex[i].Hit:
                tpmPath = self.DepthFirstSearchRecursive(i, VTo, path)
                if tpmPath.size() == 0 or tpmPath.stack[-1] == self.vertex[VTo]:
                    return tpmPath
        path.pop()
        return path

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[0]




