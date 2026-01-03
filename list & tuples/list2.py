nums = [1,2,3,4]
nums.append(5)

print(nums)

# positioning insertion 

nums.insert(1,29)
print(nums)

nums.sort()
print(nums)

# reverse sort in decreasing order

nums.sort(reverse=True)
print(nums)


nums = [10,20,30,40,50]

x = 40
idx = 0

for val in nums:
    if(val == x):
        print(f"{x} found at idx : {idx}")
        break
    idx += 1