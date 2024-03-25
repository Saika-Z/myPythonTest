import testSolution
from util import listNode
from util import treeNode

if __name__ == '__main__':
    arr = [4,3,2,7,8,2,3,1]
    ans = testSolution.findDuplicates(1, arr)
    print(f'{ans} duplicates found')
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
