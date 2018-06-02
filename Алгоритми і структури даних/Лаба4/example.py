################################################################################
#
#            prepared by Maxym_Shylo(https://github.com/Maxphy)
#
################################################################################
def binary_search(mylist, target, start, stop):
    if start > stop:
        return False
    else:
        mid =(start + stop)//2
        if target == mylist[mid]:
            return mid
        elif target < mylist[mid]:
            print(mylist[start: mid])
            return binary_search(mylist, target, start, mid-1)
        else:
            print(mylist[mid+1: stop+1])
            return binary_search(mylist, target, mid + 1, stop)

mylist = [10, 12, 14, 18, 27, 30, 33, 39, 44, 59, 62, 83, 89]
target = 27
start = 0
stop = len(mylist)
x = binary_search(mylist, target, start, stop)
if x == False:
    print("Item", target, "Not Found")
else:
    print("Item", target, "Found at Index", x)
