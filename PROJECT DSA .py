"""
@author: ASH
"""


from random import randint
class Node:
    def __init__(rbst,key,priority):
        rbst.key=key
        rbst.priority=randint(1,100)
        rbst.left=None
        rbst.right=None
    def rotate_left(rbst):
        u=rbst
        w=u.right
        u.right= w.left
        w.left=u
        u=w
        w=u.left
        return u
    def rotate_right(rbst):
        u=rbst
        w=u.left
        u.left= w.right
        w.right=u
        u=w
        w=u.right
        return u
        
        
class RBST:
    def __init__(rbst):
        rbst.root=None
    def insert(rbst,key,priority=None):
        rbst.root= rbst.__insert(rbst.root,key,priority)
        
    def __insert(rbst,root,key,priority=None):
        if root is  None:
            root=Node(key,priority)
        #return (root)
        else:    
            if key<root.key:
                root.left= rbst.__insert(root.left,key,priority)
                if root.left.priority < root.priority:
                    root = root.rotate_right()
            elif key> root.key:
                root.right=rbst.__insert(root.right,key,priority)
                if root.right.priority < root.priority:
                    root = root.rotate_left()
        return root
    
    def Search(rbst,key):
        return rbst.__Search(rbst.root,key)
    def __Search(rbst,root,key):
        if root == None:
            return False
        elif root.key == key:
            if rbst.root.key<root.key:
                return 'Found the node with value {} in tree have priority no. {} in right sub tree' .format(root.key,root.priority)
            if rbst.root.key>root.key:
                return 'Found the node with value {} in tree have priority no. {} in left sub tree' .format(root.key,root.priority)
            if rbst.root.key==root.key:
                return 'Found the node with value {} in tree have priority no. {} on root' .format(root.key,root.priority)
        l = rbst.__Search(root.left,key)
        if l:
            return True
        r = rbst.__Search(root.right,key)
        return r
    
    def Find(rbst,key):
        return rbst.__Find(rbst.root,key)
    def __Find(rbst, root,key):
        if root == None:
            return None
        if root.key == key:
            return root
        if key < root.key:
            return rbst.__Find(root.left,key)
        else:
            return rbst.__Find(root.right,key)
        
    def Delete(rbst,key):
        if rbst.Find(key) is None:
            return 'No such node with key: {} exist'.format(key)
        rbst.root = rbst.__Delete(rbst.root,key)
        return 'Node with key: {} succesfully deleted '.format(key)
    def __Delete(rbst,root,key):
        if root is None:
            return False
        if root.key == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                if root.left.priority < root.right.priority:
                    root.rotate_right()
                    root.right = rbst.__Delete(root.left,key)
                else:
                    root=root.rotate_left()
                    root.left = rbst.__Delete(root.left,key)
        elif root.key <key:
            root.right = rbst.__Delete(root.right,key)
        else:
            root.left = rbst.__Delete(root.left,key)
        return root

    def __replace(rbst, root,key,newkey):
        if root is  None:
            return False
        else:
            if root.key==key:
                root.key =newkey
            elif root.key <key:
                root.right = rbst.__replace(root.right,key,newkey)
            else:
                root.left = rbst.__replace(root.left,key,newkey)


        return root.key
        
    def replace(rbst,key,newkey) :
        if rbst.Search(key) is None:
            return 'No such node with key: {} exist'.format(key)
        rbst.root = rbst.__replace(rbst.root,key,newkey)
        return 'Node with key: {} succesfully repalced with new key {}'.format(key,newkey)
    
    def Inorder(rbst):
        rbst.__Inorder(rbst.root)
    def __Inorder(rbst,root):
        if root:
            
            rbst.__Inorder(root.left)
            print (root.key,root.priority)
            rbst.__Inorder(root.right)
    def Preorder(rbst):
        rbst.__Preorder(rbst.root)
    def __Preorder(rbst,root):
        if root:
            print (root.key,root.priority)
            rbst.__Preorder(root.left)
            
            rbst.__Preorder(root.right)
            
    def Postorder(rbst):
        rbst.__Postorder(rbst.root)
    def __Postorder(rbst,root):
        if root:
            #print (root.key,root.priority)
            rbst.__Postorder(root.left)
            rbst.__Postorder(root.right)
            print (root.key,root.priority)
            
    def Height(rbst):
        return rbst.__Height(rbst.root)
    def __Height(rbst,root):
        if root is None:
            return 0
        l=rbst.__Height(root.left)
        r=rbst.__Height(root.right)
        return 1+max(l,r)
    
    def FindMin(rbst):
         return rbst.__FindMin(rbst.root)
        
    def __FindMin(rbst,root):
        if root.left is None:
            return (root.key,root.priority)
        l=rbst.__FindMin(root.left)
        return (l)
    
    def FindMax(rbst):
         return rbst.__FindMax(rbst.root)
        
    def __FindMax(rbst,root):
        if root.right is None:
            return (root.key,root.priority)
        r=rbst.__FindMax(root.right)
        return (r)
    
    def Successor(rbst):
        return rbst.__Successor(rbst.root)
          
    def __Successor(rbst,root):
        return rbst.__FindMin(root.right)
    
    def Predessor(rbst):
        return rbst.__Predessor(rbst.root)
             
    def __Predessor(rbst,root):
        return rbst.__FindMax(root.left)


s=RBST()
s.insert(3)
s.insert (4)
s.insert(5)
s.insert(1)
print('InOrder')
s.Inorder()
print('PreOrder')
s.Preorder()
print('PostOrder')
s.Postorder()
print(s.Search(5))
print(s.Delete(6))

s.Inorder()
print('Height of a Tree: ',s.Height())
print('Minimum of a Tree: ',s.FindMin())
print('Maximum of a Tree: ',s.FindMax())
print('Successor of a Tree: ',s.Successor())
print('Predessor of a Tree: ',s.Predessor())
print(s.replace(1,2))

