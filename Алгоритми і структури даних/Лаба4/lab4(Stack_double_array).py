################################################################################
#
#            prepared by Maxym_Shylo(https://github.com/Maxphy)
#
################################################################################
class Stack(object):
    def __init__(self, max0, max1):
        self.items = [[],[]]
        self.max0 = max0
        self.max1 = max1

    def isEmpty_1(self):
        if len(self.items[0]) == 0:
            print("The stack_1 is empty!")
        else:
            print("The stack_1 is NOT empty!")

    def isEmpty_2(self):
        if len(self.items[1]) == 0:
            print("The stack_2 is empty!")
        else:
            print("The stack_2 is NOT empty!")

    def push_1(self,item):
        if len(self.items[0]) < self.max0:
            self.items[0].append(item)
        else:
            print("Stack_1 is full, cannot add any new value!")

    def push_2(self,item):
        if len(self.items[1]) < self.max1:
            self.items[1].append(item)
        else:
            print("Stack_2 is full, cannot add any new value!")

    def show_last(self):
        if (len(self.items[0]) == 0) or (len(self.items[1]) == 0):
            print("One of Stacks is EMPTY!")
        else:
             print("The last item of Stack_1:",self.items[0][-1], "of Stack_2: " ,self.items[1][-1])

    def pop_1(self):
        if len(self.items[0]) == 0:
            print("Stack_1 is empty, nothing to pop!")
        else:
            print("Deleting item from Stack_1: ",self.items[0][-1])
            self.items[0].remove(self.items[0][-1])

    def pop_2(self):
        if len(self.items[1]) == 0:
            print("Stack_2 is empty, nothing to pop!")
        else:
            print("Deleting item from Stack_2: ",self.items[1][0])
            self.items[1].remove(self.items[1][0])

    def show_stack(self):
        self.items[1].reverse()
        print(self.items[0], self.items[1])
        self.items[1].reverse()
        print(" ")
        print(" ")
        print("Length of the Stack_1 is:",len(self.items[0]),"of Stack_2: ",len(self.items[1]))

a = Stack(10,10)
for i in range (0,8):
    a.push_1(i)
for i in range (0,5):
    a.push_2(i)
print(" ")
a.show_stack()
a.pop_1()
a.pop_2()
print(" ")
a.show_last()
a.push_1(4)
a.push_1(9)
a.push_1(10)
a.push_1(11)
a.show_stack()
