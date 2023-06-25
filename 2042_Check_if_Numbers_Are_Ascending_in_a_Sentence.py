def areNumbersAscending(s: str) -> bool:
    """Function finds digits in the string and store them in a list if there is no greater
    number than itself. If nothings goes wrong it means that all the digits used in the string
    are ascendind!

    Args:
        s (str): expect contain digits

    Returns:
        bool
    """
    s = s + " "  # added white space to the end run through one xtra time the loop
    result_list = []  # digits are colloecting here int type
    temp_list = []  # digits are collecting here to see if num is multi-digit
    for char in s:  # Checking every single character + one white space we added
        if (
            char.isdigit()
        ):  # if character is digit first collecting in the temporary list
            temp_list.append(char)
        else:  # the moment we dont get digit we empty temporary list to result list
            if len(temp_list) != 0:
                a = "".join(temp_list)
                if (
                    len(result_list) > 0
                ):  # If the new number is not the largest, then we can return false
                    if int(a) > result_list[-1]:
                        result_list.append(int(a))
                        temp_list = []
                    else:
                        return False
                else:
                    result_list.append(int(a))
                    temp_list = []
            else:
                continue
    return True  # if nothing goes wrong we got true
