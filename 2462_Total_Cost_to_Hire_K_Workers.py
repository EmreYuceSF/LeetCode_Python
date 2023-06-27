from bisect import bisect_left
def totalCost(costs: list[int], k: int, candidates: int) -> int:
    """You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.

Example 1:

Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.

    Args:
        costs (list[int]): list of cost of each candidate
        k (int): num to hire
        candidates (int): candidate number for each session
    Returns:
        int: total cost
    """
    if len(costs) <= k:  #if total candidates is less than or equal to total hiring number we hire everyone and we return just total cost 
        return sum(costs)

    total_cost = 0 # otherwise we start with 0 cost and run the Algorithm

    if len(costs) > 2 * candidates:       # if total candidates is more than 2 times of candidates for each session 
        first = sorted(costs[:candidates])
        last = sorted(costs[-candidates:])
        costs = costs[candidates:-candidates]
    else:   
        if len(costs) % 2 == 0:
            first = sorted(costs[:len(costs) // 2])
            last = sorted(costs[len(costs) // 2:])
            costs = []
        else:
            first = sorted(costs[:len(costs) // 2])
            last = sorted(costs[len(costs) // 2 + 1:])
            costs = [costs[len(costs) // 2]]

    for i in range(k): 
        if len(first) > 0 and len(last) > 0:
            fl = first[0]  #lowest of sorted fist group
                

            ll = last[0] #lowest of the last group
         

            if fl <= ll: # compare of the lowest of each groups
                total_cost += fl
                first.pop(0)
                try: #if anything left in the costs list
                    insert_index = bisect_left(first, costs[0]) # finds the right index number to insert the new number from costs list
                    first.insert(insert_index, costs.pop(0))
                except IndexError:
                    continue
            elif fl > ll:
                total_cost += ll
                last.pop(0)
                try: #if anything left in the costs list
                    insert_index = bisect_left(last, costs[-1])
                    last.insert(insert_index, costs.pop())
                except IndexError:
                    continue
        elif len(first) == 0:
            try:
                min_last = min(last)
                total_cost += min_last
                last.remove(min_last)
            except:
                continue
        else:
            try:
                min_first = min(first)
                total_cost += min_first
                first.remove(min_first)
            except:
                continue

    return total_cost
