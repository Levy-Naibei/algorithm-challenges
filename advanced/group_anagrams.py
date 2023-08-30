from collections import defaultdict
def group_anagrams(strs):
   anagram_groups = defaultdict(list)
   
   for word in strs:
        # Count the frequency of each character 
        # using a character count array
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        # print(tuple(count))
        anagram_groups[tuple(count)].append(word)
   
   return list(anagram_groups.values())

print(group_anagrams(["silent","yes", "dog", "listen", "sey", "god"]))