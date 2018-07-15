'''
804. Unique Morse Code Words

International Morse Code defines a standard encoding where each letter is mapped to a series of dots 
and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. 
For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). 
We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
 

Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
'''

'''
Algorithm:
1. Iterate on each character of each words and generate morse words.
2. Save these words in a set so only unique combinations remain.
3. Return length if set

TIME COMPLEXITY: O(nk) : for 'k' words with 'n' chars
SPACE COMPLEXITY: O(nkm) : for 'k' words with 'n' chars and 'm' is the morse length of each char 
'''
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique_words = set()
        for word in words:
            morse_word = []
            for c in word:
                c_morse = morse[ord(c) - 97]
                morse_word.append(c_morse)
            unique_words.add(''.join(morse_word))
        return len(unique_words)

s = Solution()
words = ["gin", "zen", "gig", "msg"]
length = s.uniqueMorseRepresentations(words)
print(length)