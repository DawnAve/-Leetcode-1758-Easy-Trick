class Solution:
    def minOperations(self, s: str) -> int:
        check = True
        one = 0
        zero = 0
        for i in s:
            if i != str(int(check)):
                one +=1
            else:
                zero +=1
            check = not check
        return min(one,zero)
