"""
Understand:
    input: String s, String t
    output: boolean, true if two strings are anagrams(contain the same letters), false otherwise
    logic: look at 1 string, check if the lens of the strings are the same, (auto false if lens not same)
    get count of all letters in strings, compare frequncy maps
Plan:
    define function
        if len(s)!=len(t):
            return false
        freq_map = {}
        for each letter in s:
            if letter was seen b4 add 1 to its value in dict
            otherwise, add the letter as a key, and make it's value 1
        for letter in t:
            if letter not in freq_map or freq_map[letter]==0:
                return false
            subtract that letter from freq_map by 1
        return true if we make it through
    """

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_map = {}
        for letter in s:
            freq_map[letter] = freq_map.get(letter, 0) + 1

        for letter in t:
            if letter not in freq_map or freq_map[letter]==0:
                return False
            freq_map[letter] -= 1
        
        return True

        