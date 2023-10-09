#给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0
#返回所有和为 0 且不重复的三元组。

class Soulution:
    def threenum(self,nums:list[int]) ->list[list[int]]:
        nums.sort()#数组重排序降低难度
        ans=[]
        n=len(nums)
        for i in range(n):
            if nums[i]>0:
                break
            if i and nums[i]==nums[i-1]:
                continue
            j,k=i+1,n-1
            while j<k:
                x=nums[i]+nums[j]+nums[k]
                if x<0:
                    j+=1
                elif x>0:
                    k-=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return ans
                    
                    
            
