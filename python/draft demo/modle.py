#maopao
def maopao(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == '__main__':
    print(maopao([1, 5, 8, 2, 9]))

def xuanze(arr):
    lenth=len(arr)#8
    for i in range(lenth-1):
        min_dex=i #记录最小下标
        for j in range(i+1,lenth):
            if arr[min_dex]>arr[j]:
                min_dex=j
        arr[i],arr[min_dex]=arr[min_dex],arr[i]
    return arr
if __name__=='__main__':
    print(xuanze([1, 5, 8, 2, 9]))

import hashlib
def get_md5(str):
    md5=hashlib.md5(str.encode('utf-8')).hexdigest()
    return md5
if __name__ == '__main__':
    print(len(get_md5('123456')))