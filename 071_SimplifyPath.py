'''
71. Simplify Path

Given an absolute path for a file (Unix-style), simplify it. Or in other words, 
convert it to the canonical path. In a UNIX-style file system, a period . refers 
to the current directory. Furthermore, a double period .. moves the directory up 
a level. For more information, see: Absolute path vs relative path in Linux/Unix
Note that the returned canonical path must always begin with a slash /, and 
there must be only a single slash / between two directory names. The last 
directory name (if it exists) must not end with a trailing /. Also, the 
canonical path must be the shortest string representing the absolute path.

Example 1:
Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root 
level is the highest level you can go.

Example 3:
Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by 
a single one.

Example 4:
Input: "/a/./b/../../c/"
Output: "/c"

Example 5:
Input: "/a/../../b/../c//.//"
Output: "/c"

Example 6:
Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
'''

'''
ALGORITHM
The main idea is to push to the stack for every valid subpath (not in {"",".",".."}), 
1. Split path at '/'
2. For every token, ignore '', . and /
3. If, .., pop from result stack
4. append token to result
5. join result with / and return the answer 

RUNTIME COMPLEXITY: O(N) where N is the length of input path
SPACE COMPLEXITY: O(N) where N is the length of input path
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = []
        subpaths = path.split('/')
        
        for subpath in subpaths:
            if subpath == '.' or subpath == '/':
                continue
            elif subpath == '..':
                if len(result) > 0:
                    result.pop()
            elif subpath:
                result.append(subpath)
        return '/' + '/'.join(result)