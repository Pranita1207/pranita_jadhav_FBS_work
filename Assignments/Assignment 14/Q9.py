nums = [1, 2, -1, 0, -2, 1, -1]
target = 0
triplets = []

n = len(nums)
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if nums[i] + nums[j] + nums[k] == target:
                triplet = sorted([nums[i], nums[j], nums[k]])
                if triplet not in triplets:  
                    triplets.append(triplet)

print("Unique triplets:", triplets)


