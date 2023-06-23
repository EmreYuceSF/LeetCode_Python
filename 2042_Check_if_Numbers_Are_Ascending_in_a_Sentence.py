def areNumbersAscending(s: str) -> bool:
    s = s + " "
    result_list = []
    temp_list = []
    for char in s:
        if char.isdigit():
            temp_list.append(char)
        else:
            if len(temp_list) != 0:
                a = "".join(temp_list)
                if len(result_list) > 0:
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
    return result_list == sorted(result_list)


print(areNumbersAscending("4 5 3 11 26"))
