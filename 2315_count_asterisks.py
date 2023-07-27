def countAsterisks(s: str) -> int:
    tall_found = 0
    count = 0
    for char in s:
        if char == "|":
            tall_found += 1
        if not tall_found % 2:
            if char == "*":
                count += 1
    return count


print(countAsterisks("l|*e*et|c**o|*de|"))
