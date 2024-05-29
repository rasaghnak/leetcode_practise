class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        countT, countS= {},{}

        for i in range(len(s)):
            countT[t[i]]=1+countT.get(t[i],0)
            countS[s[i]]=1+countS.get(s[i],0)
        
        for c in countS:
            if countT[c]!=countS[c]:
                return False
            
        return True




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        set_var1=set()
        set_var2=set()
        for i in t:
            set_var1.add(i)
        for j in s:
            set_var2.add(j)
        check=set_var1.difference(set_var2)
        if  check==set():
            return True
        else:
            return False