#prepared by Maxym_Shylo(https://github.com/Maxphy)
import random
from random import randint

class node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

class binary_search_tree:
    def __init__(self):
        print("  ")
        print("Initialization of tree...\n")
        self.root = None

    def insert(self, value):
        print("Adding element:", value)

        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if  value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("  ")
            print("Value ", value," already in tree")
            print("  ")

    def print_tree(self, empty):
        if self.root is not None:
            self._print_tree(self.root,empty)
        else:
            print("There's no tree! Can't print tree")

    def _print_tree(self, cur_node,empty):
        if cur_node is not None:
            if cur_node.left_child is not None:
                self._print_tree(cur_node.left_child, empty +1)
            print("   "*empty,str(cur_node.value))
            if cur_node.right_child is not None:
                self._print_tree(cur_node.right_child, empty +1)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if  cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            print("The root of tree is None")

    def _search(self, value, cur_node):
        if  value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.left_child is not None:
            return self._search(value, cur_node.right_child)
        return False

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self,node):

        if node==None or self.find(node.value)==None:
            print("Node to be deleted not found in the tree!")
            return None

        def min_value_node(n):
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current

        def num_children(n):
            num_children = 0
            if n.left_child is not None:
                num_children +=1
            if n.right_child is not None:
                num_children +=1
            return num_children

        node_parent = node.parent

        node_children = num_children(node)

        #CASE_1
        #node has no  children
        if node_children == 0:
            if node_parent!=None:
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None

        #CASE_2
        #node has a single child
        if node_children ==1:

            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            if node_parent!=None:
                # replace the node to be deleted with its child
                if node_parent.left_child==node:
                    node_parent.left_child=child
                else:
                    node_parent.right_child=child
            else:
                self.root=child

            child.parent=node_parent


        #CASE_3
        #node has TWO child
        if node_children == 2:
            successor = min_value_node(node.right_child)

            node.value = successor.value
            self.delete_node(successor)



def fill_tree_1(tree, num_elem = 10, max_int = 11):
    for _ in range(num_elem):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    print("  ")
    print("  ")
    print("  ")
    print("Data type of tree is: ",type(cur_elem))
    return tree

tree = binary_search_tree()
#tree = fill_tree_1(tree)
tree.insert(27)
tree.insert(24)
tree.insert(22)
tree.insert(11)
tree.insert(42)
tree.insert(32)
tree.insert(36)
tree.insert(12)

tree.print_tree(0)
print(" ")
#tree.build_tree()
tree.delete_value(6)
tree.print_tree(0)
#print("Tree height:" +  str(tree.height()))
#print(tree.search(10))
#print(tree.search(36))