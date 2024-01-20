def jobScheduling(startTime: list[int], endTime: list[int], profit: list[int]) -> int:

    jobs = list(zip(startTime, endTime, profit))
    jobs.sort(key= lambda x: x[1])
    startTime = []
    endTime = []
    profit = []
    
    for job in jobs:
        startTime.append(job[0])
        endTime.append(job[1])
        profit.append(job[2])
    
    
    max_profit = [(profit[0],endTime[0])]
    for i in range(1, len(profit)):
        j = i-1
        while j >= 0:
            if max_profit[j][1] <= startTime[i]:
                max_profit.append((profit[i]+max(max_profit[:j+1])[0], endTime[i]))
                break
            else:
                j -= 1 
                if j == -1:
                    max_profit.append((profit[i], endTime[i]))
    return max(max_profit, key= lambda x: x[0])[0]

st = [1,2,3,3]
et = [3,4,5,6]
pt = [50,10,40,70]

print(jobScheduling(st, et, pt))

st = [1,2,3,4,6]
et = [3,5,10,6,9]
pt = [20,20,100,70,60]
print(jobScheduling(st, et, pt))


st= [4,2,4,8,2]
et = [5,5,5,10,8]
pt = [1,2,8,10,4]
print(jobScheduling(st, et, pt))