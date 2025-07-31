class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''
        for c in s:
            if c.isalnum():
                st+=c.lower()
        rev=st[::-1]
        if rev==st:
            return True
        else:
            return False