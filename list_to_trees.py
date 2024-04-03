from typing import List,Optional
class TreeNode:
    def __init__(self,val,left=None, right=None) -> None:
        self.val=val
        self.right=right
        self.left=left


def list_to_BNS(nums: List[int]) -> Optional[TreeNode]:
    def helper(start,end):
        if start>end:
            return None
        mid=(start+end)//2
        root=TreeNode(nums[mid])
        root.left=helper(start,mid-1)
        root.right=helper(mid+1,end)
        print(root.val)
    return helper(0,len(nums)-1)

#1 mid=8,start=4, end=4,    left
#2 mid=0,start=1, end=1,       left                                                  1<-3->2->4->5
#3 mid=,start=, end=, None 
# mid=,start=, end=,
# mid=,start=, end=,


list=[1,2,3,4,5]
list_to_BNS(list)


