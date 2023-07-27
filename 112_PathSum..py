

def pathSum(self, node, currentSum, targetSum):
    """
    https://leetcode.com/problems/path-sum/
    Given the root of a binary tree and an integer targetSum, 
        return true if the tree has a root-to-leaf path 
        such that adding up all the values along the path equals targetSum.

    A leaf is a node with no children.
    """
    # Base 
    if node == None:
        return False

    if node.val + currentSum == targetSum:
        return True          

    else:
        return pathSum(node.left, node.val+currentSum, targetSum) or pathSum(node.right, node.val+currentSum, targetSum)

print( pathSum(root, 0, targetSum) )