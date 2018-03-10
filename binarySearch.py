#coding:utf-8


def binarySearch(arr,index):
    head = arr[0]
    tail = arr[len(arr)-1]
    md = (head+tail)//2
    while True:
        if arr[md] == index: return 'Found'
        elif arr[md] < index:
            head = arr[md] + 1
        else:
            tail = arr[md] - 1
    if arr[md] == index: return 'Foucus'
    else; return 'NotFound'

arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
index = 10
print binarySearch(arr,index)

