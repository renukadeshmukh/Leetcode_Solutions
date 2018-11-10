'''
451. Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"
Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"
Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

'''

'''
ALGORITHM:
1. Count number of each char
2. Keep track max_count
3. Create an empty array of size max_count+1
4. Fill in the characters in this array, put each char where its count matches 
    the index in the array
5. Starting from backwords, create the result string.

RUNTIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
'''

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_cnt = 0
        char_map = {}
        for c in s:
            if c not in char_map:
                char_map[c] = 0
            char_map[c] += 1
            max_cnt = max(max_cnt, char_map[c])
        
        arr = [0]*(max_cnt+1)
        for k in char_map:
            v = char_map[k]
            if arr[v] == 0:
                arr[v] = [k*v]
            else:
                arr[v].append(k*v)
        
        res, i = [], len(arr)-1
        while i >= 0:
            if arr[i]:
                for c in arr[i]:
                    res.append(c)
            i -= 1
        
        return ''.join(res)