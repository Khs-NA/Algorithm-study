
while True:
    nums = sorted(list(map(int,input().split())))

    if max(nums) != 0:
        if min(nums) != 0:
            if nums[0]**2 + nums[1]**2 == nums[2]**2:
                print('right')
            else:
                print('wrong')

        elif min(nums) == 0 :
            print('wrong')
    else:
        break
