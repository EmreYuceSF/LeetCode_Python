def countAnagrams(s: str) -> int:
    from itertools import permutations
    import math
    from collections import Counter
    res = 1
    words = s.split(" ")
    for word in words:
        base = 1
        ln_total = len(word)
        count = Counter(list(word))
        a = math.factorial(ln_total)
        each = [x for x in count.values()] 
        for  num in each:
            base*=math.factorial(num)
        res*= (a/base)
    return int(res)

print(countAnagrams("b okzojaporykbmq tybq zrztwlolvcyumcsq jjuowpp"))