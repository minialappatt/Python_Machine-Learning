################### Program Start #######################
#array to store values of Tree
tree_values = []

# class to define element of Tree (we use common structure for BST, AVL)
# Although height is irrelevant for BST and used only in case of AVL
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1
 
 
####################################################
# function to insert key and return root in BST
def bst_insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = bst_insert(root.right, key)
        else:
            root.left = bst_insert(root.left, key)
    return root
 
# function to delete key and return root in BST
def bst_delete(root, key):
    # Base case
    if not root: return root

    if root.val > key:
        root.left = bst_delete(root.left, key)
    elif root.val < key:
        root.right = bst_delete(root.right, key)
    else:
        if not root.left: return root.right
        if not root.right: return root.left

        if root.left and root.right:
            temp = root.right
            while temp.left: temp = temp.left
            root.val = temp.val
            root.right = bst_delete(root.right, root.val)

    return root

##########################################################
#AVL tree utility functions       
def avl_Height(root):
    if not root:
        return 0
    return root.height
 
# Get balance factor of the node
def avl_BalanceFactor(root):
    if not root:
       return 0
    return avl_Height(root.left) - avl_Height(root.right)

# Get minimum value
def avl_MinValue(root):
    if root is None or root.left is None:
       return root
    return avl_MinValue(root.left)

#Left rotation
def leftRotate(b):
    a = b.right
    temp = a.left
    a.left = b
    b.right = temp
    b.height = 1 + max(avl_Height(b.left),avl_Height(b.right))
    a.height = 1 + max(avl_Height(a.left),avl_Height(a.right))
    return a
 
#Right rotation
def rightRotate(b):
    a = b.left
    temp = a.right
    a.right = b
    b.left = temp
    b.height = 1 + max(avl_Height(b.left),avl_Height(b.right))
    a.height = 1 + max(avl_Height(a.left),avl_Height(a.right))
    return a

#function to insert node in AVL tree
def avl_insert(root, key):
    if not root:
        return Node(key)
    elif key < root.val:
        root.left = avl_insert(root.left, key)
    else:
        root.right = avl_insert(root.right, key)

    root.height = 1 + max(avl_Height(root.left),avl_Height(root.right))

    # Update the balance factor and balance the tree
    balanceFactor = avl_BalanceFactor(root)
    if balanceFactor > 1:
        if key < root.left.val:
            return rightRotate(root)
        else:
            root.left = leftRotate(root.left)
            return rightRotate(root)
 
    if balanceFactor < -1:
        if key > root.right.val:
            return leftRotate(root)
        else:
            root.right = rightRotate(root.right)
            return leftRotate(root)

    return root

# function to delete node from AVL tree
def avl_delete(root, key):
    if not root:
        return root
    elif key < root.val:
        root.left = avl_delete(root.left, key)
    elif key > root.val:
        root.right = avl_delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = avl_MinValue(root.right)
        root.val = temp.val
        root.right = avl_delete(root.right, temp.val)
    if root is None:
        return root
 
    # Update the balance factor of nodes
    root.height = 1 + max(avl_Height(root.left),avl_Height(root.right))
    balanceFactor = avl_BalanceFactor(root)
 
    # Balance the tree
    if balanceFactor > 1:
        if avl_BalanceFactor(root.left) >= 0:
            return rightRotate(root)
        else:
            root.left = leftRotate(root.left)
            return rightRotate(root)

    if balanceFactor < -1:
        if avl_BalanceFactor(root.right) <= 0:
            return leftRotate(root)
        else:
            root.right = rightRotate(root.right)
            return leftRotate(root)
    return root

############################################################################
# Function to find and print level and position of node key in Tree(BST/AVL)
def printLevelandPosition(root, key):
 
    # Base Case
    if (root == None):
        return
 
    # Create an empty queue
    q = []
 
    # Enqueue Root and initialize height
    q.append(root)
 
    # Create and initialize current level and position by 1
    currLevel,position = 1,1
 
    while (len(q) != 0):
        size = len(q)
        while (size != 0):
 
            node = q[0]
            q = q[1:]
 
            # print if node data equal to key
            if (node.val == key):
                print("level",currLevel,"and its position is",position,"from the left",file=file2)
         
            # increment the position
            position += 1
 
            # Enqueue left child
            if (node.left != None):
                q.append(node.left)
 
            # Enqueue right child
            if (node.right != None):
                q.append(node.right)
             
            size -= 1
 
        # increment the level
        currLevel += 1
        position = 1

##################################################
# function to do preorder traversal of Tree (BST/AVL)
def preorder(root):
    if root:
        # add element into store array
        tree_values.append(root.val)
        print(root.val,end=" ",file=file2)
        preorder(root.left)
        preorder(root.right)

###################################################
#main control starts from here

file1 = open('inputPS03.txt', 'r')
file2 = open('outputPS03.txt', 'w')

Lines = file1.readlines()
#we will store all 3 lines data in input array
input = []
for line in Lines:
    # Find the position of the opening curly brace and the closing curly brace
    start_index = line.find('{')
    end_index = line.find('}')

    # Extract the substring containing the array
    array_string = line[start_index + 1:end_index]

    # Split the array string by commas and convert the strings to integers
    input.append([int(num.strip()) for num in array_string.split(',')])


#set root element
bst = Node(input[0][0])
avl = Node(input[0][0])

#insert remaining elements of first input line(week1)
for item in input[0][1:] :
    bst = bst_insert(bst, item)
    avl = avl_insert(avl, item)

print("End of week 1 - Acceptances",file=file2)
print("Preorder traversal of the constructed BST tree is [",end=" ",file=file2)
preorder(bst)
print("]",file=file2)
print("Preorder traversal of the constructed AVL tree is [",end=" ",file=file2)
preorder(avl)
print("]",file=file2)
print("\n",file=file2)

#week2 items addition
for item in input[1] :
    bst = bst_insert(bst, item)
    avl = avl_insert(avl, item)
    
print("End of week 2 – With new acceptances",file=file2)
print("Preorder traversal of the rearranged BST tree is [",end=" ",file=file2)
preorder(bst)
print("]",file=file2)
print("Preorder traversal of the re-arranged AVL tree is [",end=" ",file=file2)
preorder(avl)
print("]",file=file2)
print("\n",file=file2)

#week2 items deletion
for item in input[2] :
    bst = bst_delete(bst, item)
    avl = avl_delete(avl, item)

tree_values = []
print("End of week 2 – After declines",file=file2)
print("Preorder traversal of the rearranged BST tree is [",end=" ",file=file2)
preorder(bst)
print("]",file=file2)
print("Preorder traversal of the re-arranged AVL tree is [",end=" ",file=file2)
preorder(avl)
print("]",file=file2)
print("\n",file=file2)

# get 3 random values
import random
random_values = random.sample(tree_values, 3)

print("Randomly selected three volunteers =",random_values,file=file2)

#import time

#print position of randomply selected items
print("BST:",file=file2)
#start_time = time.perf_counter()
for r in random_values :
    print("Employee #",r,"is present in",end=" ",file=file2)
    printLevelandPosition(bst, r)
#print(time.perf_counter()-start_time)

print("AVL:",file=file2)
#start_time = time.perf_counter()
for r in random_values :
    print("Employee #",r,"is present in",end=" ",file=file2)
    printLevelandPosition(avl, r)
#print(time.perf_counter()-start_time)

file1.close()
file2.close()
#################### Program End #######################