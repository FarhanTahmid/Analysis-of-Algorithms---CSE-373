jobs = [('job1', 4, 20), ('job2', 1, 10), ('job3', 1, 40), ('job4', 1, 30)]
total_profit, job_sequence = schedule_jobs_brute_force(jobs)
print(total_profit)  # 60
print(job_sequence)  # ['job3', 'job1', 'job4']