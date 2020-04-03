'''
394. Decode String
'''

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        ans = ''
        stack = ['']
        i = 0

        while i < len(s):
            if s[i] == '[':
                stack.append('[')
                stack.append('')
                i += 1
            elif s[i] == ']':
                while stack[-1] != '[':
                    strng = stack.pop()
                    if stack[-1][0].isdigit():
                        stack[-1] = strng * int(stack[-1])
                    else:
                        stack[-1] = stack[-1] + strng  
                i += 1
            else:
                if stack and stack[-1].isalpha() and s[i].isdigit():
                    stack.append(s[i])
                elif i > 0 and s[i-1] == ']':
                    stack.append(s[i])
                else:
                    stack[-1] += s[i]
                i += 1
        
        
        while len(stack) > 1:
            strng = stack.pop()
            if stack[-1][0].isdigit():
                stack[-1] = strng * int(stack[-1])
            else:
                stack[-1] = stack[-1] + strng  
        
        return stack[0]



s = Solution()
print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
print(s.decodeString("3[a]2[bc]"))
print(s.decodeString("3[a2[c]]"))
print(s.decodeString("2[abc]3[cd]ef"))
#s = "2[abc]3[cd]ef"



