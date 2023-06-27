def totalCost(costs: list[int], k: int, candidates: int) -> int:
    if len(costs) <= k:
        return sum(costs)

    total_cost = 0

    if len(costs) > 2 * candidates:
        first = sorted(costs[:candidates])
        last = sorted(costs[-candidates:])
        costs = costs[candidates:-candidates]
    else:
        if len(costs) % 2 == 0:
            first = sorted(costs[: len(costs) // 2])
            last = sorted(costs[len(costs) // 2 :])
            costs = []
        else:
            first = sorted(costs[: len(costs) // 2])
            last = sorted(costs[len(costs) // 2 + 1 :])
            costs = [costs[len(costs) // 2]]

    for i in range(k):
        if len(first) > 0 and len(last) > 0:
            fl = first[0]
            fi = 0

            ll = last[0]
            li = 0

            if fl <= ll:
                total_cost += fl
                first.pop(fi)
                try:
                    insert_index = bisect_left(first, costs[0])
                    first.insert(insert_index, costs.pop(0))
                except IndexError:
                    continue
            elif fl > ll:
                total_cost += ll
                last.pop(li)
                try:
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
