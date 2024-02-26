from typing import List

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)

        return list(anagrams.values())


assert sorted(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])) == sorted(
    [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
)
assert Solution().groupAnagrams(strs=[""]) == [[""]]
assert Solution().groupAnagrams(strs=["a"]) == [["a"]]
