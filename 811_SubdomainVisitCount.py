'''
811. Subdomain Visit Count
'''

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_map = {}
        for domain in cpdomains:
            arr = domain.split(' ')
            address_arr = arr[1].split('.')
            i, last, cnt = -2, address_arr[-1], 1
            
            while cnt <= len(address_arr):
                domain_map = self.add_to_map(domain_map, last, int(arr[0]))
                if cnt != len(address_arr):
                    last = '.'.join([address_arr[i], last])
                cnt += 1
                i -= 1
        print(domain_map)
                        
        result = []       
        for entry in domain_map:
            result.append("{0} {1}".format(domain_map[entry], entry))
        return result
            

    def add_to_map(self, domain_map, key, cnt): 
        if key in domain_map:
            domain_map[key] += cnt
        else:
            domain_map[key] = cnt
        return domain_map

s = Solution()
ip = ["9001 discuss.leetcode.com"]
res = s.subdomainVisits(ip)
print(res)

ip = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
res = s.subdomainVisits(ip)
print(res)
