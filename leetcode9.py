# solution 1 

number="-123"
list=[]
for i in number:
    list.append(i) 
rev_num=""
k=len(list)-1
while (k>=0):
    rev_num += list[k]
    k-=1
print(rev_num)
if rev_num==number:
    print("true")
else:
    print("false")

# solution 2 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        number=str(x)
        list=[]
        for i in number:
            list.append(i)
        rev_num=""
        k=len(list)-1
        while (k>=0):
            rev_num+=list[k]
            k-=1
        if rev_num==number:
            return("true")
        else:
            return("false")
        
# Create an instance of Solution
solution = Solution()

# Call the isPalindrome method with the instance
result = solution.isPalindrome(-121)
print(result)  # Output: False

# solution 3

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        num=str(x)
        reversed_number=num[::-1]

        return reversed_number==num
        

