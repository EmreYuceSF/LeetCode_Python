def isHappy(n: int) -> bool:
    """_summary_

    Args:
        n (int): _description_

    Returns:
        bool: _description_
    """
    n_str = str(n)
    n_list = list(n_str)
    check_list = [n_str]
    while len(n_list) != 1 or n_list[0] != "1":
        new_num = 0
        for num in n_list:
            new_num += int(num)**2
        n_list = list(str(new_num))
        if str(new_num) not in check_list:
            check_list.append(str(new_num))
        else:
            return False
    return True

