from collections import defaultdict
def combine_anagrams(words_array):
    anagrams = defaultdict(list)
    for word in words_array:
        sorted_w = ''.join(sorted(word.lower()))
        anagrams[sorted_w].append(word)
    return list(anagrams.values())
print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"]))