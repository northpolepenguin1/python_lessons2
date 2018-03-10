#coding:utf-8

def linearSearch(arr,index):
    cnt = 0
    for i in range(len(arr)):
        if arr[cnt] == index:
            return 'Found!'
        elif arr[cnt] != index:
        else:
            return 'Not Found'
arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
index = 10
print linearSearch(arr,index)

