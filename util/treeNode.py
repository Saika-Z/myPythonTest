class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def StrToIntArray(s):
    strs = s.split(",")
    arr = []
    for i in range(len(strs)):
        if strs[i] == "null":
            arr.append(float("inf"))
        else:
            arr.append(int(strs[i]))
    return arr


def mkTree(s):
    arr = StrToIntArray(s)
    nodes = [None] * (len(arr) + 1)
    for i in range(1, len(nodes)):
        if arr[i - 1] != float("inf"):
            nodes[i] = TreeNode(arr[i - 1])
        else:
            nodes[i] = None

    for i in range(1, len(nodes) // 2):
        node = nodes[i]
        if node is None:
            continue
        node.left = nodes[2 * i]
        node.right = nodes[2 * i + 1]
    return nodes[1]


def beforeTraverse(treeNode):
    """前序遍历（根->左->右）"""
    if treeNode is None:
        return [None]
    elif treeNode.left is None and treeNode.right is None:
        return [treeNode.val]
    else:
        return [treeNode.val] + beforeTraverse(treeNode.left) + beforeTraverse(treeNode.right)


def afterTraverse(treeNode):
    """后序遍历（左->右->根）"""
    if treeNode is None:
        return [None]
    elif treeNode.left is None and treeNode.right is None:
        return [treeNode.val]
    else:
        return afterTraverse(treeNode.left) + afterTraverse(treeNode.right) + [treeNode.val]

def sequenceTraverse(treeNode):
    """层序遍历"""
    arrayList = []
    nodes = [treeNode]
    arrayList.append(treeNode.val)

    while nodes:
        subNodes = []
        for value in nodes:
            if value.left or value.right:
                if value.left:
                    subNodes.append(value.left)
                    arrayList.append(value.left.val)
                else:
                    arrayList.append(None)
                if value.right:
                    subNodes.append(value.right)
                    arrayList.append(value.right.val)
                else:
                    arrayList.append(None)
        nodes = subNodes

    return arrayList