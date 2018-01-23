import random

nums , single_d, double_d = ([],[],[])
for i in range(10):
    nums.append(random.randint(1,40))
print(nums)

def get_single_digits(num):
    if len(str(num)) == 1:
        single_d.append(num)

def get_double_digits(num):
    if len(str(num)) == 2:
        double_d.append(num)

def sort_single_d_array():
    if len(single_d) >= 2:
        for i in range(len(single_d)):
            for j in range(i+1,len(single_d)):
                if single_d[i] < single_d[j]:
                    temp = single_d[i]
                    single_d[i] = single_d[j]
                    single_d[j] = temp
    else:
        print('single_d lenght not Enought.')

def sort_double_d_array():
    if len(double_d) >= 2:
        for i in range(len(double_d)):
            for j in range(i+1,len(double_d)):
                if double_d[i] < double_d[j]:
                    temp = double_d[i]
                    double_d[i] = double_d[j]
                    double_d[j] = temp
    else:
        print('double_d length not Enought.')

def compare_the_arrays():
    ch = ''
    for i in range(len(single_d)):
        sort_big = []
        equa = []
        for j in range(len(double_d)):
            ch = str(double_d[j])
            if single_d[i] > int(ch[0]):
                sort_big.append(int(ch))
            else:
                if single_d[i] == int(ch[0]):
                    equa.append(int(ch))

            #khask tkaml hna tkaml htimalat khad append l array akhra
            #sghir o kbir thaz


        if len(sort_big) > 0:
            print('sort bg = ',sort_big)

        if len(equa) > 0:
            print('equa = ',equa)


big_num = ''
for j in range(len(nums)):
    if nums[j] == 9:
        big_num += str(nums[j])

    get_single_digits(nums[j])
    get_double_digits(nums[j])

sort_single_d_array()
sort_double_d_array()

print('single = ',single_d)
print('double = ',double_d)

compare_the_arrays()







