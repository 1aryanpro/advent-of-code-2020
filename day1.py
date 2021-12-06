input = open("inputs/day1.txt", 'r').read().split('\n')
nums = list(map(int, input[:-1]))
size = len(nums)

#  for i in range(size):
    #  for j in range(i+1, size):
        #  if nums[i] + nums[j] == 2020:
            #  print(nums[i] * nums[j])
            #  break

for i in range(size):
    for j in range(i+1, size):
        for k in range(j+1, size):
            if nums[i] + nums[j] + nums[k] == 2020:
                print(nums[i] * nums[j] * nums[k])
                break
