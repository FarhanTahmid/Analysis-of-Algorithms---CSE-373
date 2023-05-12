import itertools

def schedule_jobs_brute_force(jobs):
    # generate all possible permutations of the given jobs
    job_permutations = itertools.permutations(jobs)
    
    # initialize the maximum profit and the sequence of jobs
    max_profit = 0
    max_job_sequence = []
    
    # for each permutation, compute the profit and select the one with the maximum profit
    for job_sequence in job_permutations:
        # initialize the boolean array indicating whether a slot is available or not
        n = max(job_sequence, key=lambda x: x[1])[1]
        slots = [True] * n
        
        # initialize the total profit
        total_profit = 0
        
        # traverse through the jobs in the current permutation
        for job in job_sequence:
            # starting from the deadline of the current job, check if there is a slot available
            for i in range(job[1]-1, -1, -1):
                if slots[i]:
                    # if there is a slot available, mark the slot as unavailable
                    slots[i] = False
                    # add the profit of the current job to the total profit
                    total_profit += job[2]
                    break
                    
            # if no slot is available, ignore the current job
                    
        # select the permutation with the maximum profit
        if total_profit > max_profit:
            max_profit = total_profit
            max_job_sequence = [job[0] for job in job_sequence]
            
    return max_profit, max_job_sequence

jobs = [('job1', 4, 20), ('job2', 1, 10), ('job3', 1, 40), ('job4', 1, 30)]
total_profit, job_sequence = schedule_jobs_brute_force(jobs)
print(total_profit)  # 60
print(job_sequence)  # ['job3', 'job1', 'job4']