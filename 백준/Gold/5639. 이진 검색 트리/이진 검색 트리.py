import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
pre = []
for line in sys.stdin:
    pre.append(int(line.strip()))

tree = {}

def make_tree(pre):
    if not pre:
        return None
    
    root_val = pre[0]
    root = Node(root_val)
    
    check = len(pre)
    for i in range(1,len(pre)):
        if  pre[i] > root_val:
            check = i
            break
        
    root.left = make_tree(pre[1:check])
    root.right = make_tree(pre[check:len(pre)])
    
    return root

def postorder(tree):
    if tree:
        
        postorder(tree.left)
        postorder(tree.right)
        print(tree.val)

        
x = make_tree(pre)  
postorder(x)
