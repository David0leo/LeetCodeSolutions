"""
The general idea here is a single pass algorithm that
starts with the first element, iterates through the rest, 
and takes the longest common prefix substring from subsequent 
elements.

More formally in pseudocode:
Given array S = {s1, s2, ..., sn}, of strings, define:

LONGEST-COMMON-PREFIX(S)
    Prefix = S[1]
    for i = 2 to S.length
        for j = 0 to Prefix.length
            if j > S[i].length or S[i][j] != Prefix[j]
                Prefix = Prefix[1, 2, ..., j - 1]
                break
    return Prefix
    
Note that we assume S is not empty. We can put a check in to
handle the case that S is empty. Also note where most of the
work gets done in. In the inner loop (L13 - L16), we are 
performing O(min(S[i].length, Prefix)) operations each time
we do this loop, which is S.length - 1 times. 
We can speed this up in many cases by setting Prefix to be
the smallest string in S. This means we will be doing minimal
comparisons with every other string. 

On LeetCode making this small change increased speed by 14% !
LeetCode can be inconsistent with its times, but this was a 
definite improvement just by passing over S once. 
"""

def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs:
            #trace once to find minimal elem
            length = len(strs)
            inf = 0
            
            for i in range(1, length):
                if len(strs[i]) < len(strs[inf]):
                    inf = i
            
            #have minimal elem at index inf
            prefix = strs[inf]
            for j in range(length):
                if j == inf:
                    continue
                for k in range(len(prefix)):
                    if strs[j][k] != prefix[k]:
                        prefix = prefix[:k]
                        break
            return prefix
                
        return ''
