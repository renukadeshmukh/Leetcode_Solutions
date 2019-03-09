'''
535. Encode and Decode TinyURL

TinyURL is a URL shortening service where you enter a URL such as 
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as 
http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no 
restriction on how your encode/decode algorithm should work. You just need to 
ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded 
to the original URL.
'''

'''
ALGORITHM:
1. Maintain a storage to save longurl <-> shorturl mapping
2. To encode, generate next unique integer and map it with long url(length of
   storage)
3. From short url, extract the integer and return the longurl at this index

RUNTIME COMPLEXITY: 
    encode: O(N) as len function will take liner time to find length of storage
    decode: O(1)
SPACE COMPLEXITY:
    encode: O(N) to save urls lookup
    decode: O(1)
'''
class Codec:
    def __init__(self):
        self.storage = []
        
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.storage.append(longUrl)
        return 'http://tinyurl.com/' + str(len(self.storage)-1)
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        index = int(shortUrl.split('/')[-1])
        return self.storage[index]


