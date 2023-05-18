import random
from collections import namedtuple

import random

def generate_random_jobs(N):
    job_id_range = (1, 1000)
    deadline_range = (1, 200)
    profit_range = (0, 500)

    jobs = []

    for _ in range(N):
        job_id = random.randint(job_id_range[0], job_id_range[1])
        deadline = random.randint(deadline_range[0], deadline_range[1])
        profit = random.randint(profit_range[0], profit_range[1])
        job_tuple = (job_id, deadline, profit)
        jobs.append(job_tuple)

    return jobs

n=int(input())
jobs=generate_random_jobs(n)
print(jobs)