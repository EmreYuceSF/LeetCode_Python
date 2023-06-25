def generate(numRows: int) -> list[list[int]]:
    """Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
                           1
                          1  1
                        1  2  1
                      1  3  3   1
                    1  4  6   4  1

    """
    res = []
    for num in range(1, numRows + 1):
        res.append([1] * num)

    if numRows > 2:
        for i in range(1, len(res) - 1):
            for j in range(len(res[i]) - 1):
                res[i + 1][j + 1] = res[i][j] + res[i][j + 1]
    return res
