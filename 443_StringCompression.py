'''
443. String Compression

Given an array of characters, compress it in-place. The length after compression 
must always be smaller than or equal to the original array. Every element of the 
array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of 
the array.

Follow up:
Could you solve it using only O(1) extra space?

Example 1:
Input:
["a","a","b","b","c","c","c"]
Output:
Return 6, and the first 6 characters of the input array should be: 
["a","2","b","2","c","3"]
Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 
Example 2:
Input:
["a"]
Output:
Return 1, and the first 1 characters of the input array should be: ["a"]
Explanation:
Nothing is replaced.

Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output:
Return 4, and the first 4 characters of the input array should be: 
["a","b","1","2"].
Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is 
replaced by "b12". Notice each digit has it's own entry in the array.

Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
'''

'''
ALGORITHM:
1. Keep 2 pointers i and j. Pointers i iterates over the chars array. Pointers j 
   keep track of the compressed array. 
2. Keep incrementing i till similar characters are found. Then write the character
   and its count at j and j+1 locations. (If count > 9 then convert count to 
   string and write the count character by character.)
3. Return the position of j as final length of result array. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i, j = 0, 0
        while i < len(chars):
            x = chars[i]
            count = 0
            while i < len(chars) and chars[i] == x:
                i += 1
                count += 1
            
            chars[j] = x
            j += 1
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1
        return j