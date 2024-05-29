# To know if the list contains duplicate numbers, I used the same concept as the valid anagram, Hashing really helps in this matter

nums=[1,2,3,4]
countN={}

final= "True"
for i in range(len(nums)):
    countN[nums[i]]=1+countN.get(nums[i],0)

for c in countN:
    if countN[c] > 1:
        continue
    else:
        final="False"

print(final)


