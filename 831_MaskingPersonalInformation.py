'''
831. Masking Personal Information

We are given a personal information string S, which may represent either an email 
address or a phone number. We would like to mask this personal information 
according to the following rules:


1. Email address:
We define a name to be a string of length ≥ 2 consisting of only lowercase 
letters a-z or uppercase letters A-Z. An email address starts with a name, 
followed by the symbol '@', followed by a name, followed by the dot '.' and 
followed by a name. All email addresses are guaranteed to be valid and in the 
format of "name1@name2.name3". To mask an email, all names must be converted to 
lowercase and all letters between the first and last letter of the first name 
must be replaced by 5 asterisks '*'.

2. Phone number:
A phone number is a string consisting of only the digits 0-9 or the characters 
from the set {'+', '-', '(', ')', ' '}. You may assume a phone number contains 
10 to 13 digits. The last 10 digits make up the local number, while the digits 
before those make up the country code. Note that the country code is optional. 
We want to expose only the last 4 digits and mask all other digits. The local 
number should be formatted and masked as "***-***-1111", where 1 represents the 
exposed digits. To mask a phone number with country code like "+111 111 111 1111", 
we write it in the form "+***-***-***-1111".  The '+' sign and the first '-' sign 
before the local number should only exist if there is a country code.  For 
example, a 12 digit phone number mask should start with "+**-". Note that 
extraneous characters like "(", ")", " ", as well as extra dashes or plus signs 
not part of the above formatting scheme should be removed. 

Return the correct "mask" of the information provided.
'''

'''
ALGORITHM:
1. If S[0] is char mask_email else mask_phone
2. if email or phone, use string manipulation to mask characters.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if S[0].isalpha():
            return self.mask_email(S)
        else:
            return self.mask_phone(S)
            
    def mask_email(self, email):
        email = email.lower()
        parts = email.split('@')
        parts[0] = parts[0][0] + '*****' + parts[0][-1]
        return '@'.join(parts)
    
    def mask_phone(self, phone):
        phone = phone.replace(')', '').replace('(', '').replace(' ', '').
                    replace('-', '').replace('+', '')
        last4 = phone[-4:]
        if len(phone) > 10:
            m = '*' * (len(phone) - 10)
            return '+' + m +'-***-***-' + last4
        else:
            return '***-***-' + last4