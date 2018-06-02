################################################################################
#
#            prepared by Maxym_Shylo(https://github.com/Maxphy)
#
################################################################################
class Node:
    def __init__(self, key = None, Next = None, Prev = None):
        self.key = key
        self.Next = Next
        self.Prev = Prev
class Linked_List(object):
    def __init__(self,max_len):
        self.Head = None
        self.Tail = None
        self.max_len = max_len

    def Len(self):
        tmp_len = 0
        if self.Head is not None:
            new_Node = self.Head
            tmp_len += 1
            while new_Node.Next is not self.Tail:
                new_Node = new_Node.Next
                tmp_len += 1
        return tmp_len+1

    def Enqueue(self,key):
        if self.Len() < self.max_len:
            new_Node = Node(key, None, None)
            if self.Head is None:
                self.Head = new_Node
            else:
                self.Tail.Next = new_Node
            self.Tail = new_Node
            self.Head.Prev = self.Tail
            self.Tail.Next = self.Head
        else:
            print("The circular queue is full!")

    def show_queue(self):
        print("Your queue now is: ")
        new_Node = self.Head
        while new_Node is not self.Tail:
            print(new_Node.key)
            new_Node = new_Node.Next
        print(self.Tail.key)
        print("The max len of circular queue is:", self.max_len)


    def show_el(self):
        if self.Head is not None:
            new_Node_1 = self.Head.Prev
            new_Node_2 = self.Tail.Next
            print("The self.Head.Prev element of queue is: ",new_Node_1.key)
            print("The self.Tail.Next element of queue is: ",new_Node_2.key)
        else:
            print("The queue is empty")

    def Dequeue(self):
        if self.Head is not None:
            self.Head = self.Head.Next
            self.Head.Prev = self.Tail
            self.Tail.Next = self.Head
        else:
            print("The queue is empty")

    def show_w_el(self):
        k = input("Type el: ")
        if self.Head is not None:
            new_Node = self.Head
            i = 1
            for i in range(1,k+1):
                new_Node = new_Node.Next
                if i == k-1:
                    print("The element:",new_Node.key)

a = Linked_List(13)
for i in range(0, 14):
    a.Enqueue(i)
a.show_queue()
print("The shape of your queue now is: ",a.Len())
a.show_el()
a.Dequeue()
a.show_queue()
a.show_el()
a.show_w_el()
#a.show_first()
