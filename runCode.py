import testSolution
from util import listNode
from util import treeNode

if __name__ == '__main__':
    arr = [1, 2, -3, 3, 1]
    ans = listNode.createlistNode(1, arr)
    aa = testSolution.removeZeroSumSublists(1,ans)
    listNode.printlistnode(1, aa)
    # tree = testSolution.removeZeroSumSublists(1, ans, 2)
    # listNode.printlistnode(1, tree)
    # tree = treeNode.mkTree("1,2,3,4,5,null,6,7,8,null,10")
    # t1 = treeNode.beforeTraverse(tree)
    # t2 = treeNode.afterTraverse(tree)
    # t3 = treeNode.sequenceTraverse(tree)
    # print(f"tree is {t1}")
    # print(f"tree is {t2}")
    # print(f"tree is {t3}")
    # print(treeNode.sequenceTraverse.__doc__)
