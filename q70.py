# 爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

def ClimbStairs(n):
    num=0
    if n==1:
        num=1
    elif n==2:
        num=2
    else:
        num=ClimbStairs(n-1)+ClimbStairs(n-2)
    return num

print(ClimbStairs(4))

#正确
