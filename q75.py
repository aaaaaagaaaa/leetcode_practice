# 颜色分类
# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，
# 使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 必须在不使用库内置的 sort 函数的情况下解决这个问题。

def SortColor(num):
    n=len(num)
    for k in range(0,n):
        for i in range(0,n-1):
            if num[i]>num[i+1]:
                num[i+1],num[i]=num[i],num[i+1]#置换相邻数
    return num 
              
print(SortColor([2,0,2,1,1,0]))