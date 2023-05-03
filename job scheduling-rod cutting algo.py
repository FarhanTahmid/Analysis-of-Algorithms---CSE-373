def job_scheduling_rc(jobs, machines):
    n = len(jobs)
    m = len(machines)
    lengths = [machines[j+1] - machines[j] for j in range(m-1)]
    lengths.append(float('inf'))

    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = float('inf')
        for j in range(i):
            dp[i] = min(dp[i], dp[j] + sum(max(jobs[k][p]*lengths[p], 0) for k in range(j, i)) )

    return dp[n]

def main():
    jobs = [(3, 2, 1), (2, 3, 4), (1, 2, 3), (4, 3, 2)]
    machines = [1, 3, 5, 6]

    result = job_scheduling_rc(jobs, machines)
    print("Minimum completion time:", result)

if __name__ == '__main__':
    main()
