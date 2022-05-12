# Method 1 using Hash Tables
def validAnagram(s:str,t:str) -> bool:
    if len(s)!=len(t):
        return False
    sMap,tMap = {},{}

    for i in range(len(s)):
        sMap[s[i]] = 1 + sMap.get(s[i],0)
        tMap[t[i]] = 1 + tMap.get(t[i],0)

    for c in sMap:
        if sMap[c] != tMap.get(c,0):
            return False

    return True

# Memory complexity is O(1)
def validAnagramSorting(s: str, t:str) -> bool:
    return sorted(s) == sorted(t)


# input

s = 'rat'
t = 'cat'

p= 'anagram'
q= 'nagaram'

print(validAnagram(p,q))
print(validAnagramSorting(p,q))