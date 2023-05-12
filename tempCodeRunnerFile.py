jobs = [('job1', 3, 3), ('job2', 1, 140), ('job3', 1, 40), ('job4', 1, 60),
        ("Job A", 2, 6), ("Job B", 6, 4), ("Job C", 7, 2), ("Job D", 1, 5), ("Job E", 5, 11)]
total_profit, job_sequence = schedule_jobs(jobs)
print(total_profit)  # 60
print(job_sequence)  # ['job3', 'job1', 'job4']