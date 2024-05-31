#Two sum II leetcode
#Two pointer concept 

List = [1,2,3,4]
target = 3

f=0
l=len(List)-1
while(f<l):
    sum=List[f]+List[l]
    if sum==target:
        print(f"{f},{l} indexs")
    elif sum<target:
        f+=1
    else:
        l-=1
print(f"{f},{l} final out")


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f=0
        l=len(numbers)-1
        while(f<l):
            if (numbers[f]+numbers[l])==target:
                return [f+1,l+1]
            elif (numbers[f]+numbers[l])<=target:
                f+=1
            else:
                l-=1
        return [f+1,l+1]


        
