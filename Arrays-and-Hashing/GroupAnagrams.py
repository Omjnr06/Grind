# Given an array of strings, group all the anagrams together. THe answer can be returned in any order
def GroupAnagrams(strings):
    hashmap = {}

    for x in range(len(strings)):
        key = "".join(sorted(strings[x]))
        if key in hashmap:
            hashmap[x].append(strings[x])
        else:
            hashmap[x] = [strings[x]]

    return list(hashmap.values())