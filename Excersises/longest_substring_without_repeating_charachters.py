"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_counter = defaultdict(int)
        max_ss = 0
        start = 0
        end = 0
        
        while end < len(s):
            char_counter[s[end]] += 1
            
            while char_counter[s[end]] > 1:
                char_counter[s[start]] -= 1
                start += 1

            max_ss = max(end - start + 1, max_ss)
            end += 1
        
        return max_ss