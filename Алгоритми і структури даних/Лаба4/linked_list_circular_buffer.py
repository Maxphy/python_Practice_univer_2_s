################################################################################
#
#            prepared by Maxym_Shylo(https://github.com/Maxphy)
#
################################################################################
class Node:
    def __init__(self, key = None, Next = None):
        self.key = key
        self.Next = Next

class Linked_List:

    def __init__(self):
        self.Head = None
        self.Tail = None


    def Len(self):
        tmp_len = 0
        if self.Head is not None:
            new_Node = self.Head
            tmp_len += 1
            while new_Node.Next is not None:
                new_Node = new_Node.Next
                tmp_len += 1
        return tmp_len

    def Enqueue(self,key):
        new_Node = Node(key, None)
        if self.Head is None:
            self.Head = new_Node
        else:
            self.Tail.Next = new_Node
        self.Tail = new_Node
        self.Tail.Next = self.Head

    def show_queue(self):
        print("Your queue now is: ")
        new_Node = self.Head
        while new_Node is not self.Tail:
            print(new_Node.key)
            new_Node = new_Node.Next
        print(self.Tail.key)

    def show_first(self):
        if self.Head is not None:
            new_Node = self.Tail.Next
            print("The self.Tail.Next element of queue is: ",new_Node.key)
        else:
            print("The queue is empty")

    def Dequeue(self):
        if self.Head is not None:
            self.Head = self.Head.Next
        else:
            print("The queue is empty")


a = Linked_List()
for i in range(0, 11):
    a.Enqueue(i)
a.show_queue()
#print("The shape of your queue now is: ",a.Len())
a.show_first()
#a.Dequeue()
#a.show_queue()
#a.show_first()
