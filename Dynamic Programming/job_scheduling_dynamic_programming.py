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


def getJobProfit(job):
    return job[2]

def getJobDeadline(job):
    return job[1]

def jobSchedulingWithDynamicProgramming(jobs):
    # Sort jobs in descending order based on profits
    jobs.sort(key=getJobProfit, reverse=True)

    
    # getting the maximum deadline of jobs
    maximumDeadline = max(jobs, key=getJobDeadline)[1]
    #define a dynamic array for bottom up process  
    dynamic = [0] * (maximumDeadline+1)
    #createing job sequence with max deadline
    jobSequence = [''] * (maximumDeadline+1)

    # Traverse through the jobs at first in bottom up approach
    for job in jobs:
        deadline = job[1]
        profit = job[2]

        # Find the earliest available slot for the current job
        while deadline > 0 and dynamic[deadline] != 0:
            deadline -= 1

        # Update dynamic array and jobSequence lists to sort the jobs in order
        if deadline > 0:
            dynamic[deadline] = profit
            jobSequence[deadline] = job[0]

    # Find the maximum profit and the corresponding job sequence that will be performed seuentially
    maximumProfit = sum(dynamic)
    maximumJobSequence = []
    for job in jobSequence:
        if job != '':
            maximumJobSequence.append(job)

    return maximumProfit, maximumJobSequence

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
    maxProfit,jobSequence=jobSchedulingWithDynamicProgramming(jobs=jobs)
    print(f"Max profit will be: {maxProfit}")
    print(f"Job sequence of Execution will be: {jobSequence}")
    endOfExecution=time.time()
    timeRequired.append(round(endOfExecution-startOfExecution,4))