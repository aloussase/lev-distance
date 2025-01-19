"""
Edit distance algorithm.

Authors:

- Alexander Goussas
- Luis Bajana
- Juan Antonio Gonzalez
- Ariana Palacios
- Piero Valentino
"""

from functools import lru_cache

def levenshtein_distance(str1: str, str2: str) -> int:
    # This is what does the caching
    @lru_cache
    def lev(i: int, j: int) -> int:
        # Base cases
        if i == 0: return j
        if j == 0: return i
            
        # If characters are the same, no operation needed
        if str1[i-1] == str2[j-1]:
            return lev(i-1, j-1)
            
        return 1 + min(
            lev(i-1, j),    # deletion from str1
            lev(i, j-1),    # insertion into str1
            lev(i-1, j-1)   # substitution in str1 from str2
        )
    
    return lev(len(str1), len(str2))


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 3:
        str1 = sys.argv[1]
        str2 = sys.argv[2]
    else:
        str1, str2, *rest = sys.stdin.readlines()

    dist = levenshtein_distance(str1, str2)

    print(dist)
