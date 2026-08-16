def maopao(arr):
    n=len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):  #比较次数
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
            print(f"i={i},j={j},交换后的数组：{arr}")
        if not swapped:
            break
        print(f"第{i+1}轮情况！")
    return arr
if __name__ == '__main__':
    maopao([8,11,9,5,4])

#any检查元素是否存在
c=[8,11,9,5,4]
if any(x==50 for x in c) == True:
   print('存在！')
else:
    print('不存在')


