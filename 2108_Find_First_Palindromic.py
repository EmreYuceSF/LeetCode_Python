def sumFourDivisors(nums: list[int]) -> int:
    total = 0
    for num in nums:
        checker = []
        if num == 6:
            total += 12
        elif num < 6:
            pass
        else:
            if not num % 2:
                checker.append(1)
                checker.append(num)
                checker.append(2)
                checker.append(int(num / 2))
                top_limit = int(num / 3)
                for i in range(3, top_limit):
                    if int(num / i) / (num / i) == 1:
                        break
                total += sum(checker)
            else:
                checker.append(1)
                checker.append(num)
                top_limit = int(num / 3)
                for i in range(3, top_limit, 2):
                    if int(num / i) / (num / i) == 1:
                        checker.append(i)
                        if int(num / i) != i:
                            checker.append(int(num / i))
                            top_limit = int(num / i)
                        else:
                            break
                if len(checker) == 4:
                    total += sum(checker)

    return total


print(sumFourDivisors([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
