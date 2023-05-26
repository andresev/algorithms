from collections import defaultdict


def groupAnagrams(strs: list[str]):
    anagram_groups = defaultdict(list)

    for word in strs:
        sort_word = ''.join(sorted(word))
        anagram_groups[sort_word].append(word)

    print(anagram_groups.values())
    return list(anagram_groups.values())
