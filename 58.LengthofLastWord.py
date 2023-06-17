def lengthOfLastWord(s: str) -> int:
    """Given a string s consisting of words and spaces, return the length of the last word in the string.

    A word is a maximal substring consisting of non-space characters only.

    Example 1:

    Input: s = "Hello World"
    Output: 5
    Explanation: The last word is "World" with length 5.
    """
    s = s[
        ::-1
    ].lstrip()  # Reverse the sentence and remove the white space from the begining (left)
    if (
        " " not in s
    ):  # if there is no white space in the string it means whole string is a word
        return len(s)
    else:
        i = s.index(
            " "
        )  # index(" ") will find the first space in the string and this index will be equal to length of the first word
        return i
