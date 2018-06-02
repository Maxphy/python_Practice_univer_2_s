################################################################################
#
#            prepared by Maxym_Shylo(https://github.com/Maxphy)
#
################################################################################
class Node:
    def __init__(self, key = None, Prev = None, Next = None):
        self.key = key
        self.Prev = Prev
        self.Next = Next

class Linked_List(object):
    def __init__(self,Length):
        self.Head = None
        self.Tail = None
        self.Length = 0

    def Len(self):
        g = 0
        if self.Head is not None:
            g +=1
            new_Node = self.Head
            while new_Node.Next is not None:
                g +=1
                new_Node = new_Node.Next
            return g

    def Enqueue(self,key):
        #if self.g > self.Length:
        new_Node = Node(key, None, None)
        new_Node.key = key
        new_Node.Prev = None
        if self.Head is not None:
            new_Node.Next = self.Head
            self.Head.Prev = new_Node
            self.Head = new_Node
        else:
            self.Head = self.Tail = new_Node
        #else:
            #print("Stack is full, cannot add any new value!")

    def show_queue(self):
        print("Your queue now is: ")
        new_Node = self.Head
        while new_Node:
            print(new_Node.key)
            new_Node = new_Node.Next

    def show_first(self):
        if self.Head is not None:
            print("The last element of queue is: ",self.Tail.key)
        else:
            print("The queue is empty")

    def Dequeue(self):
        if self.Tail is not None:
            self.Tail = self.Tail.Prev
            self.Tail.Next = None
        else:
            print("The queue is empty")


a = Linked_List(10)
for i in range(0,11):
    a.Enqueue(i)
a.show_queue()
print("The shape of your queue now is: ",a.Len())
a.show_first()
a.Dequeue()
a.show_queue()
