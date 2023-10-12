class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        Time Complexity: O(nklog k) 
           where k = maximum length of string
                 n = size of strs array.
            Each string is sorted in time = O(k log k)
            Iteration through the loop = n
        Space Complexity: O(nk)

        Did this code successfully run on Leetcode: Yes
    
        Any problem you faced while coding this: No
    
        Intuition: Each sorted string is the hash-key, and the original string is added to the list of values
        """
        # Brute force approach - sort each string and stick it in a hash 
        result = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in result:
                result[sorted_str].append(str)
            else:
                result[sorted_str] = [str] # this is what sets up the object as a list, as opposed to a string
        
        return list(result.values())

            

        
