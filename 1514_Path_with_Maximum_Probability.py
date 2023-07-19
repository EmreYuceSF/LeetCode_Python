def maxProbability(n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
    start_points = []
    end_points = []
    res = []
    
    
    for i in range(len(edges)):
        if start in edges[i]:
            start_points.append(i)
        elif end in edges[i]:
            end_points.append(i)
            
        
    ...
    