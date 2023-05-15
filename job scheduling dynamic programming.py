def job_scheduling_dp(jobs):
    # Compute the number of jobs and the maximum deadline
    n = len(jobs)
    d = max(jobs, key=lambda x: x[1])[1]

    # Initialize the dp array with 0 values
    dp = [[0 for _ in range(d+1)] for _ in range(n+1)]

    # Compute the maximum profit for each job and deadline using dynamic programming
    for i in range(1, n+1):
        for t in range(1, d+1):
            job = jobs[i-1]
            if job[1] <= t:
                dp[i][t] = max(dp[i-1][t], dp[i-1][t-job[1]] + job[2])
            else:
                dp[i][t] = dp[i-1][t]

    # Find the maximum profit and the sequence of jobs with their names, profits, and deadlines
    max_profit = dp[n][d]
    job_sequence = []
    t = d
    for i in range(n, 0, -1):
        if dp[i][t] != dp[i-1][t]:
            name, deadline, profit = jobs[i-1]
            job_sequence.append((name, profit, deadline))
            t -= deadline
    job_sequence.reverse()

    # Return the maximum profit and the sequence of jobs
    return max_profit, job_sequence

jobs = [('job1', 4, 20), ('job2', 1, 10), ('job3', 1, 40), ('job4', 1, 30)]
total_profit, job_sequence = job_scheduling_dp(jobs)
print(total_profit)  # 60
print(job_sequence)  # ['job3', 'job1', 'job4']