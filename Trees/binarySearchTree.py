class Tree:
    # constructor for the tree structure
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def insert(root, data):
    # check if root is null to insert
    if root == None:
        return Tree(data)
    # else traverse the binary tree
    else:
        if data == root.val:
            return root
        elif data <= root.val:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    
    return root

def search(root, data):
    # if empty tree, return false
    if root == None:
        print(str(data) + " not found.")
        return False
    # else traverse tree until data is found
    else:
        if root.val == data:
            print("found " + str(data) + ".")
            return True 
        elif root.val <= data:
            root.right = search(root.right, data)
        else:
            root.left = search(root.left, data)

def inOrderTraversal(root):
    # left --> visit curr --> right
    if root:
        inOrderTraversal(root.left)
        print(root.val)
        inOrderTraversal(root.right)

def preOrderTraversal(root):
    # visit curr --> left --> right
    if root:
        print(root.val)
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)
        

def postOrderTraversal(root):
    # left --> right --> visit curr
    if root:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.val)

def main():
    newTree = Tree(20)

    newTree = insert(newTree, 50)
    newTree = insert(newTree, 2)
    newTree = insert(newTree, 1)
    newTree = insert(newTree, 17)
    newTree = insert(newTree, 23)
    newTree = insert(newTree, 9)

    print("inorder:")
    inOrderTraversal(newTree)
    
    print("\npre order:")
    preOrderTraversal(newTree)

    print("\npost order:")
    postOrderTraversal(newTree)

    print("\nsearch for 50:")
    newTree = search(newTree, 50)

if __name__ == "__main__":
    main()
    