#以空间换时间-两数之和：时间、空间复杂度均为O(N)
def TwoSum(nums:list[int],target:int) ->list[int]:
    dic={}
    for i in range(len(nums)):
        if target-nums[i] in dic:
            return [dic[target-nums[i]],i]
        dic[nums[i]]=i
print(TwoSum([1,2,3,4,5,6],7))