# 背！！！
# 用class定义树节点
class TreeNode:
    # 初始化val值，左子树和右子树
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

# 构建最大二叉树
def Max_BT(nums):
    # 如果数组为空则返回空树
    if not nums:
        return None
    # 先用max函数求出数组中的最大值
    Max_val=max(nums)
    # 然后再用index函数求出最大值所在的位置
    Max_index=nums.index(Max_val)
    # 创建根节点
    root=TreeNode(Max_val)
    # 递归创建左子树
    root.left=Max_BT(nums[:Max_index])
    # 递归创建右子树
    root.right=Max_BT(nums[Max_index+1:])
    return root

# 先序遍历，根-左-右
def preOrder(root):
    # 如果节点为空，就返回null
    if not root:
        return 'null'
    # 判断当前节点是否为叶子节点
    if not root.left and not root.right:
        return root.val
    # 递归遍历左子树
    left_str = preOrder(root.left)
    # 递归遍历右子树
    right_str = preOrder(root.right)
    # 使用f“”进行字符串格式化输出
    return f"{root.val} {left_str} {right_str}"

# 先从IO中读取输入
nums = list(map(int,input().split()))
# 建立最大二叉树
root = Max_BT(nums)
# 按照先序遍历打印二叉树的值
print(preOrder(root))
