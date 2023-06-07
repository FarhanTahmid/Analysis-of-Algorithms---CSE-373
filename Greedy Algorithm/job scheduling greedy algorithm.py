import random
import time
import matplotlib.pyplot as plt

def generateRandomJobs(n):
    
    jobs = []

    for i in range(n):
        job_id = random.randint(1,1000)
        deadline = random.randint(1, 2000)
        profit = random.randint(0,500)
        job_tuple = (job_id, deadline, profit)
        jobs.append(job_tuple)

    return jobs

def get_job_deadline(job):
    return job[1]

def jobSchedulingUsingGreedy(jobs):
    # Sort the jobs in descending order of profit
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    # Initialize the total profit and the sequence of jobs
    total_profit = 0
    job_sequence = []

    # Initialize the slots indicating whether a deadline is available or not
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    slots = [False] * (max_deadline + 1)

    # Schedule the jobs
    for job in jobs:
        deadline = job[1]

        # Find the available slot closest to the deadline
        while deadline > 0 and slots[deadline]:
            deadline -= 1

        if deadline > 0:
            slots[deadline] = True
            total_profit += job[2]
            job_sequence.append(job[0])

    return total_profit, job_sequence

def resultOfAlgorithm(numberOfJobs,timeRequired):
    #plotting the graph
    plt.plot(numberOfJobs,timeRequired)
    
    plt.xlabel("Number Of Jobs")
    plt.ylabel("Time Required")
    plt.title("Job Scheduling with Brute Force Algorithm")
    plt.show()

print("Note: Enter 0 to end the program and generate Results")

#initializing matrix for number of jobs and time required
listNumber0fJobs=[]
timeRequired=[]

while True:
    #Enter number of jobs you want to generate
    numberOfJobs=int(input("Enter the number of jobs you want to generate: "))
    if(numberOfJobs==0):
        resultOfAlgorithm(numberOfJobs=listNumber0fJobs,timeRequired=timeRequired)
        break
    print(numberOfJobs)
    listNumber0fJobs.append(numberOfJobs)

    #Generate random jobs using functions
    jobs=generateRandomJobs(numberOfJobs)
    
    startOfExecution=time.time()
    #implementing brute force Algorithm
    maxProfit,jobSequence=jobSchedulingUsingGreedy(jobs=jobs)
    print(f"Max profit will be: {maxProfit}")
    print(f"Job sequence of Execution will be: {jobSequence}")
    endOfExecution=time.time()
    timeRequired.append(round(endOfExecution-startOfExecution,4))
    

    
    
        

