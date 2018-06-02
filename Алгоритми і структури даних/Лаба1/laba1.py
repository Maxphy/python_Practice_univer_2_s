################################################################################
#
#            prepared by Maxym_Shylo(https://github.com/Maxphy)
#
################################################################################
"""
#Пример рекурсии
def privet(x):
    if x ==0:
        return
    else:
        print("hello world")
        privet(x-1)

privet(4)

#Факториал числа
n = input("Факториал числа ")
n = int(n)
def sum(x):
    if x>0:
        if x == 0:
            return 1
        else:
            return x * sum(x - 1)
    else:
       return None

z=sum(n)
print(z)

#Фиббоначи

def fido(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    elif x == 3:
        return 1
    else:
        return fido(x-1) + fido(x-2)


print(fido(5));


#Бинарный поиск(поиск в отсортированном массиве)
#iskomoe искомое число
#start начальный елемент
#stop последний елемент
#mid элемент который равен свмме стопа и старта деленное на два(целое число)

def binarysearch(mylist, iskomoe, start, stop):
    if start > stop:
        return False
    else:
        mid =(start + stop)//2
        if iskomoe == mylist[mid]:
            return mid
        elif iskomoe < mylist[mid]:
            return binarysearch(mylist, iskomoe, start, mid-1)
        else:
            return binarysearch(mylist, iskomoe, mid + 1, stop)


mylist = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 73, 81]

iskomoe = 20
start =0
stop =len(mylist)

x = binarysearch(mylist, iskomoe, start, stop)

if x == False:
    print("Item", iskomoe, "Not Found")
else:
    print("Item", iskomoe, "Found at Index",x)



#Поднесение в положительный целый степень действительное ненулевое число
def calc(x, n):
    if n==0:
        return 1
    elif x > 0 and n > 0 and isinstance(n, int) == True:
        return x*calc(x,n-1)
    else:
        print("ERROR: These numbers are not supported in program.")

print("The answer: ",calc(2,7))

#Алгоритм Евклида
# Theory

#Алгоритм Евклида – это алгоритм нахождения наибольшего общего делителя (НОД) пары целых чисел.
#Наибольший общий делитель (НОД) – это число, которое делит без остатка два числа и делится само без остатка на любой другой делитель данных двух чисел.

def nsd(a,b):
    if b ==0:
        return a
    else:
        return nsd(b,a % b)

print(nsd(36,45))

#Ханойские башни. Алгоритм

def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)

moveTower(2, "A", "B", "C")




#Сортировка вставками

def insertion_sort(arrayToSort):
    a = arrayToSort
    for i in range(len(a)):
        v = a[i]
        j = i;
        while (a[j-1] > v) and (j > 0):
            a[j] = a[j-1]
            j = j - 1
        a[j] = v
        print (a)
    return a

ary = [54,1,2,3,52,3,1,2,3,5,3,67,3,2,543]
print (insertion_sort(ary))


#Shell_sort(Сортировка шелла)

import numpy as np


def shellsort(a):
    def new_increment(a):
        i = int(len(a) / 2)
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(np.round(i / 2.2))
            yield i

    for increment in new_increment(a):
        for i in range(increment, len(a)):
            for j in range(i, increment - 1, -increment):
                if a[j - increment] < a[j]:
                    break
                a[j], a[j - increment] = a[j - increment], a[j]
                print(a)
    return a
list = [9,6,5,4,3,2,12]
print(shellsort(list))

#Fibbonacci
def fido(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x == 3:
        return 1
    else:
        return fido(x-1) + fido(x-2)

k=7
s = 0
for i in range(0, k):
    print(fido(i))
    s = s +fido(i)
print(s)
"""
#Bubble Sort/ Сортировка пузырьком(модернизированный алгоритм)
oldlist = [10, 75, 43, 15, 25, -4, 27]

def bubble_sort(mylist):
    last_item = len(mylist) - 1
    for z in range(0, last_item):
        for x in range(0, last_item-z):
            print(mylist)
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x + 1] = mylist[x + 1], mylist[x]
    return mylist


print("Old List: ", oldlist)
newlist = bubble_sort(oldlist).copy()
print("New List: ", newlist)
