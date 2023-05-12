def schedule_jobs(jobs):
    # sort the jobs in descending order of their profit
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    
    # initialize the boolean array indicating whether a slot is available or not
    n = max(jobs, key=lambda x: x[1])[1]
    slots = [True] * n
    
    # initialize the total profit and the sequence of jobs
    total_profit = 0
    job_sequence = []
    
    # traverse through the sorted jobs list
    for job in jobs:
        # starting from the deadline of the current job, check if there is a slot available
        for i in range(job[1]-1, -1, -1):
            if slots[i]:
                # if there is a slot available, mark the slot as unavailable
                slots[i] = False
                # add the profit of the current job to the total profit
                total_profit += job[2]
                # add the current job to the sequence of jobs
                job_sequence.append(job[0])
                break
                
        # if no slot is available, ignore the current job
                
    return total_profit, job_sequence

jobs = [('job1', 3, 3), ('job2', 1, 140), ('job3', 1, 40), ('job4', 1, 60),
        ("Job A", 2, 6), ("Job B", 6, 4), ("Job C", 7, 2), ("Job D", 1, 5), ("Job E", 5, 11)]
total_profit, job_sequence = schedule_jobs(jobs)
print(total_profit)  # 60
print(job_sequence)  # ['job3', 'job1', 'job4']
