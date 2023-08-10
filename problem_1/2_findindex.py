def findArray(nums):
    max = -10000000000000000000
    index = -1
    for i in range(0,len(nums)):
        if(nums[i] > max):
            max = nums[i]
            index = i
    return max,index
s1 = [1,2,1,3,5,6,4]
s2 = [-1,-4,5]
max,index = findArray(s2)
print(f"max = : {max}, index : {index} ")