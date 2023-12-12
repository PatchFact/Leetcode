# get input
nums = input("Input array of numbers as comma separated list: ")

# filter not numbers and split commas
nums = nums.split(",")

duplicate = False

for i in range(len(nums)):
    
    counter = 0

    for f in range(len(nums)):
        if nums[i] == nums[f]:
            counter += 1
    
    if counter >= 2:
        duplicate = True
        break

print(duplicate)