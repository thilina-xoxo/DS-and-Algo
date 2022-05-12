
#two pointers soltion
class solution:
    def isPalindrome(self, s:str) -> bool:
        l,r = 0, len(s)-1

        while l<r:
            while l<r and not self.Numaric(s[l]):
                l=l+1
            while r>l and not self.Numaric(s[r]):
                r = r-1

            if(s[l].lower()!=s[r].lower()):
                return False
            l,r = l+1, r-1
            return True

    def Numaric(self,c):
        return (ord('A') <= ord('c') <= ord('Z')) or \
               (ord('a') <= ord('c') <= ord('z')) or \
               (ord('1') <= ord('c') <= ord('9'))

# extra memory with in build funcitons
    def isPalindromeInBuild(self, s:str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]

# hash table method, if we use two hash tables extra memory is needed ; just for try

    def isPalindromeHashTable(self,s: str) -> bool:

        return True







# check
sol = solution()

nam = 'thilina'
print(sol.isPalindrome(nam))
print((sol.isPalindromeInBuild(nam)))

