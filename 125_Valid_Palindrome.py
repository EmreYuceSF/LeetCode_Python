def isPalindrome(s: str) -> bool:
    """******************************
    function takes string char by char and if char alpha or num
    collects in a list then compare it to reverse of it.

    Args:
        s (str): string (can have any character and white space)

    Returns:
        bool: return true if reversed list is equal to original list
        *****************************
    """
    lst = []
    for a in s:
        if a.isanum():
            lst.append(a.lower())

    return lst == lst[-1::-1]
