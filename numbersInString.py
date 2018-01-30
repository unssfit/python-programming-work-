# https://www.codewars.com/kata/numbers-in-strings
# link problem

def solve(string):
    nums, num = [], ''
    for i in range(len(string)):
        if string[i].isdigit():
            num += string[i]
        else:
            if num != '':
                nums.append(int(num))
            num = ''
    nums.append(int(num))
    #print(nums)
    # get the largest number
    for j in range(1,len(nums)):
        if nums[0] < nums[j]:
            temp = nums[0]
            nums[0] = nums[j]
            nums[j] = temp
    print(nums[0])

solve('gh12cdy695m1ss4007')

