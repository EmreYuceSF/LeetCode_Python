def longestCommonSubsequence(text1: str, text2: str) -> int:
    column, row = len(text1), len(text2)
    matrix = [[False]*column]*row
    for i in range(column):
        for j in range(row):
            if text1[i] == text2[j]:
                matrix[j][i] = True
                break
                
    for row in matrix:
        print(row)
    
longestCommonSubsequence("abcde", "ace")