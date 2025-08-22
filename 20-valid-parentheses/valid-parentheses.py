class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==1:
            return False
        mystack = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                mystack.append(s[i])
            elif s[i]==')' and len(mystack)!=0:
                x = mystack.pop()
                if x!='(':
                    return False
            elif s[i]=='}' and len(mystack)!=0:
                x=mystack.pop()
                if x!='{':
                    return False
            elif s[i]==']' and len(mystack)!=0:
                x = mystack.pop()
                if x != '[':
                    return False
            else:
                return False

        if len(mystack)>0:
            return False
        return True


        