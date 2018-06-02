################################################################################
#
#            prepared by Maxym_Shylo(https://github.com/Maxphy)
#
################################################################################
class Queue(object):
    def __init__(self,max):
		self.items = []
		self.max = max

    def isEmpty(self):
        if len(self.items) == 0:
            print("The Queue is empty!")
        else:
            print("The Queue is NOT empty!")

    def isFull(self):
        if len(self.items) == self.max:
            print("The Queue is FULL!")
        else:
            print("The Queue is NOT FULL")

    def Enqueue(self,item):
        if len(self.items) < self.max:
            self.items.insert(0,item)
        else:
            print("Queue is full, cannot add any new value!")

    def show_First(self):
        if len(self.items) == 0:
            print("Queue is EMPTY!")
        else:
             print("The first item is: ",self.items[-1])

    def Dequeue(self):
        if len(self.items) == 0:
            print("Queue is empty, nothing to pop!")
        else:
            print("Deleting item: ",self.items[-1])
            self.items.remove(self.items[-1])

    def show_Queue(self):
        for items in self.items:
            print(items)
        print("Length of the Queue is:",len(self.items))

a = Queue(10)
for i in range(0,4):
    a.Enqueue(i)
print(" ")
a.show_Queue()
print(" ")
a.show_First()
print(" ")
a.Dequeue()
print(" ")
a.show_Queue()
print(" ")
a.show_First()
