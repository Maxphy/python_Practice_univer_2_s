################################################################################
#
#            prepared by Maxym_Shylo(https://github.com/Maxphy)
#
################################################################################
l = [7,3,6,1,0]

def linear_search(list, value):
    for i in range(0, len(list)):
        if list[i] == value:
            return i
    return -1

print(linear_search(l, 56))
