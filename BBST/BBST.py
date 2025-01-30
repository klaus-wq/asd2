def GenerateBBSTArray(a):
    if len(a) == 0:
        return a
    a.sort()
    tree = [None] * len(a)
    return GenerateBBSTArrayRecursive(a, tree, 0)

def GenerateBBSTArrayRecursive(a, tree, index):
    middleIndex = len(a) // 2
    tree[index] = a[middleIndex]
    left = a[:middleIndex]
    if len(left) > 0:
        GenerateBBSTArrayRecursive(left, tree, index * 2 + 1)
    right = a[middleIndex + 1:]
    if len(right) > 0:
        GenerateBBSTArrayRecursive(right, tree, index * 2 + 2)
    return tree