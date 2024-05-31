# # def compare_characters(s: str) -> bool:    
s="No lemon, no melon"
newS=""

for i in s:
    if i.isalnum():
        newS+=i.lower()
        
print(newS)

f=0
l=len(newS)-1

    # print(newS[l])

while f<=l:
    if newS[f]==newS[l]:
        f+=1
        l-=1
    else:
        print("False")
        
print("True")



