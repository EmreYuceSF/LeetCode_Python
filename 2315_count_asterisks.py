def countAsterisks(s: str) -> int:
    """You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.

    """
    tall_found = 0
    count = 0
    for char in s:  # O(n) time complexity
        if char == "|":   
            tall_found+=1
        if not tall_found%2:
            if char == "*":
                count +=1
    return count
print(countAsterisks("l|*e*et|c**o|*de|"))

            