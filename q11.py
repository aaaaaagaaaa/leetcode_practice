#q11.乘最多水的容器

arr=input("")
height=[int(n) for n in arr.split(",")]

def max_vol(height):
    n=len(height)
    arr=[]
    for i in range(0,n-1):
        arr.append([min(height[i],height[j])*(j-i) for j in range(i+1,n)])
    return max(arr) 

print(max_vol(height))   
