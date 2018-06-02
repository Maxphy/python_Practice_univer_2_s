#import something

class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

class  BinarySearchTree(object):
    """docstring for  BinarySearchTree"""
    def __init__(self):
        super( BinarySearchTree, self).__init__()
        self.twins = []
        self.root = None
        

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.inNode(self.root,data)

    def inNode(self,node,data):
        if node.left is None and node.right is None:
            if data > node.data:
                newNode = Node(data)
                node.right = newNode
            else:
                newNode = Node(data)
                node.left = newNode
        else:
            if data > node.data:
                if node.right is not None:
                    self.inNode(node.right,data)
                else:
                    newNode = Node(data)
                    node.right = newNode
            else:
                if node.left is not None:
                    self.inNode(node.left,data)
                else:
                    newNode = Node(data)
                    node.left = newNode


    def print_Tree(self,root,level):  # Вывод дерева.
        if(root.data):
            if root.left is not None:
                self.print_Tree(root.left,level + 1);
            print("   "*level,root.data)
            if root.right is not None:
                self.print_Tree(root.right,level + 1);

    def count_twins(self,root,data):
        if data in self.twins:
            return 0
        
        else:
            if root is None:
                return 0
            else:
                if root.left is not None and root.right is not None:
                    return int(data == root.data) + self.count_twins(root.left,data) + self.count_twins(root.right,data)
                elif root.left is not None and root.right is None:
                    return int(data == root.data) + self.count_twins(root.left,data)
                elif root.right is not None and root.left is None:
                    return int(data == root.data) + self.count_twins(root.right,data)
                else:
                    return int(data == root.data)
            

    def find_twins(self,root):
        
        count = self.count_twins(root = root,data = root.data)
        count = count - 1
        if count is not None and count != 0:
            for i in range(count):
                self.twins.append(root.data)
                print("Added ",root.data)

        if root.left is not None and root.right is not None:
            return self.find_twins(root.left) and self.find_twins(root.right)
        elif root.left is not None and root.right is None:
            return self.find_twins(root.left)
        elif root.right is not None and root.left is None:
            return self.find_twins(root.right)
        else:
            return True

    def erase_twins(self):

        for data in self.twins:
            self.erase(self.root,data)


    def minimum(self,root):
        if root.left is None:
            return root
        return self.minimum(root.left)

    def erase(self,root,data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.erase(root.left,data)
        elif data > root.data:
            root.right = self.erase(root.right,data)
        elif root.left is not None and root.right is not None:
            root.data = self.minimum(root.right).data
            root.right = self.erase(root.right,root.data)

        else:
            if root.left is not None:
                root = root.left

            else:
                root = root.right
        return root

    def post_ord(self,root):
        if root is None:
            return

        self.post_ord(root.left)
        self.post_ord(root.right)
        print(root.data)

 

def main():
    pchar = "k"
    bst = BinarySearchTree()
    bst.insert(pchar)
    bst.print_Tree(root = bst.root,level = 0)
    for i in range(10):
        pchar = input()
        bst.insert(pchar)
    print("Postorder traversal: ___BEGIN___")
    bst.post_ord(bst.root)
    print("___END___")
    bst.print_Tree(root = bst.root, level = 0)
    bst.find_twins(root = bst.root)
    print(bst.twins)
    bst.erase_twins()
    bst.print_Tree(root = bst.root, level = 0)
    print(bst.root.data)
if __name__ == "__main__":
    main()