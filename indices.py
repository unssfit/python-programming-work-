

target = 9
nums = [4,5,6,8,72,2,34,5]

for i in range(len(nums)-1):
    if nums[i] + nums[i+1] >= target:
        print(i,i+1)

        