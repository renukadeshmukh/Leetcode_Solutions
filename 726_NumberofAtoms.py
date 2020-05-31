'''
726. Number of Atoms

Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more 
lowercase letters, representing the name.
1 or more digits representing the count of that element may follow if the count 
is greater than 1. If the count is 1, no digits will follow. For example, H2O 
and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, 
H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a 
formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following 
form: the first name (in sorted order), followed by its count (if that count is 
more than 1), followed by the second name (in sorted order), followed by its 
count (if that count is more than 1), and so on.

Example 1:
Input: 
formula = "H2O"
Output: "H2O"
Explanation: 
The count of elements are {'H': 2, 'O': 1}.

Example 2:
Input: 
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: 
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:
Input: 
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: 
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

Note:
1. All atom names consist of lowercase letters, except for the first character 
  which is uppercase.
2. The length of formula will be in the range [1, 1000].
3. formula will only consist of letters, digits, and round parentheses, and is a 
valid formula as defined in the problem.
'''

'''
ALGORITHM:
1. multiplier = 1, foctors = [], elem = '', cnt = 1
2. Start with end of the formula
3. If formula[i] is digit, keep decrementing i, till entire difit is found. 
4. If formula[i] is ')', increase multiplier by a factor of cnt (num after ')')
5. If formula[i] is '(', increase multiplier by a factor of cnt. (num after ')')
6. If formula[i] is char, if formula[i] is upper case, elem is formula[i], else
   elem is formula[i-1] + formula[i]. 
7. Once all elements are counted, sort alphabetically and add the elem counts. 
8. Return string format of elem and counts. 

RUNTIME COMPLEXITY: O(NLogN) for sorting
SPACE COMPLEXITY:  O(N)
'''

from collections import defaultdict
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """

        store = defaultdict(int)
        
        multiplier = 1
        factors = []
        cnt = 1
        elem = ''
        i = len(formula)-1
        while i >= 0:
            c = formula[i]
            if c == ')':
                factors.append(cnt)
                multiplier *= cnt
                cnt = 1
            elif c == '(':
                multiplier /= factors[-1]
                factors.pop()
            elif c.isdigit():
                cnt = self.getElementCount(formula, i)
                i -= len(cnt)-1
                cnt = int(cnt)
                #print(cnt)
            elif c.isalpha():
                elem = self.getElementName(formula, i)
                if c.islower():
                    i -= 1
                store[elem] += (cnt * multiplier)
                cnt = 1
                #print( elem)
                
            i -= 1

        answer = ''
        for k in sorted(store):
            answer += k
            if store[k] > 1:
                answer += str(store[k])
        return answer
            


        
            
    def getElementName(self, formula, i):
        elem = ''
        if formula[i].islower():
            elem = formula[i-1] + formula[i]
        else:
            elem = formula[i]
        return elem
    
    def getElementCount(self, formula, i):
        j = i
        while formula[j].isdigit():
            j -= 1
        return formula[j+1:i+1]


s = Solution()
print(s.countOfAtoms("K4(ON(SO3)2)2"))
print(s.countOfAtoms("Mg(OH)2"))
            