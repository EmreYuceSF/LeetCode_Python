def firstPalindrome(words: list[str]) -> str:
    """
    ************************
    function checks words from the list and if word palindrome returns it!

    Args:
        words (list[str]): list if string

    Returns:
        first palindrome in the lists (String)

    """
    result = ""
    for word in words:
        if word == word[-1::-1]:
            return word
    return result
