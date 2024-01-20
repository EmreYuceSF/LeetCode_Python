def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
    ln = len(answerKey)
    res = 0

    def find_max(a=0):
        temp = 0

        nonlocal ln, res, answerKey, k
        replace = k
        for i in range(a, ln):
            if answerKey[i] == answerKey[a]:
                temp += 1
            elif answerKey[i] != answerKey[a]:
                if replace > 0:
                    if replace == k:
                        a_ = i
                    temp += 1
                    replace -= 1

                elif replace == 0:
                    res = max(res, temp)
                    if a_ < ln - res:
                        find_max(a_)
                        break
                    else:
                        break
        if replace > 0 and i == ln - 1:
            c = a

            while a > 0 and replace > 0:
                replace -= 1
                a -= 1
                if answerKey[a] != answerKey[c]:
                    temp += 1
                else:
                    break
        res = max(res, temp)

    find_max()
    return res


print(maxConsecutiveAnswers("FFFTTFTTFT", 3))
