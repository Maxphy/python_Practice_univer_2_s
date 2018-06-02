################################################################################
#
#            prepared by Maxym_Shylo(https://github.com/Maxphy)
#
################################################################################
class Stack(object):
    def __init__(self,max):
		self._items = []
		self._max = max

    def isEmpty(self):
        if len(self._items) == 0:
            print("The stack is empty!")
        else:
            print("The stack is NOT empty!")

    def isFull(self):
        if len(self._items) == self._max:
            print("The stack is FULL!")
        else:
            print("The stack is NOT FULL")

    def push(self,item):
        if len(self._items) < self._max:
            self._items.append(item)
        else:
            print("Stack is full, cannot add any new value!")

    def show_last(self):
        if len(self._items) == 0:
            print("Stack is EMPTY!")
        else:
             print("The last item is: ",self._items[-1])

    def pop(self):
        if len(self._items) == 0:
            print("Stack is empty, nothing to pop!")
        else:
            print("Deleting item: ",self._items[-1])
            self._items.remove(self._items[-1])

    def show_stack(self):
        for _items in reversed(self._items):
            print(_items)
        print("Length of the stack is:",len(self._items))


a = Stack(11)
a.isEmpty()
for i in range(0,7):
    a.push(i)
a.show_stack()
print(" ")
a.pop()
a.show_stack()
#print(" ")
#for i in range(7,8):
#    a.push(i)
#print(" ")
#a.show_stack()
#a.push('g')
#print(" ")
#a.show_stack()
#a.show_last()
#a.push('new')
