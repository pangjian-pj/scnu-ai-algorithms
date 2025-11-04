class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def Max_BT(nums):
    if not nums:
        return None
    Max_val=max(nums)
    Max_index=nums.index(Max_val)
    root=TreeNode(Max_val)
    root.left=Max_BT(nums[:Max_index])
    root.right=Max_BT(nums[Max_index+1:])
    return root

def preOrder(root):
    if not root:
        return 'null'
    if not root.left and not root.right:
        return root.val
    left_str = preOrder(root.left)
    right_str = preOrder(root.right)
    return f"{root.val} {left_str} {right_str}"

nums = list(map(int,input().split()))
root = Max_BT(nums)
print(preOrder(root))
