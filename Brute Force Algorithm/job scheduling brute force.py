import itertools
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

def jobSchedulingUsingBruteForce(jobs):
    # Generate all possible permutations of the given jobs
    job_permutations = itertools.permutations(jobs)

    # Initialize the maximum profit and the sequence of jobs
    max_profit = 0
    max_job_sequence = []

    # For each permutation, compute the profit and select the one with the maximum profit
    for job_sequence in job_permutations:
        # Initialize the boolean array indicating whether a slot is available or not
        n = max(job_sequence, key=get_job_deadline)[1]
        slots = [True] * n

        # Initialize the total profit
        total_profit = 0

        # Traverse through the jobs in the current permutation
        for job in job_sequence:
            # Starting from the deadline of the current job, check if there is a slot available
            for i in range(job[1] - 1, -1, -1):
                if slots[i]:
                    # If there is a slot available, mark the slot as unavailable
                    slots[i] = False
                    # Add the profit of the current job to the total profit
                    total_profit += job[2]
                    break

            # If no slot is available, ignore the current job

        # Select the permutation with the maximum profit
        if total_profit > max_profit:
            max_profit = total_profit
            max_job_sequence = [job[0] for job in job_sequence]

    return max_profit, max_job_sequence

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
    maxProfit,jobSequence=jobSchedulingUsingBruteForce(jobs=jobs)
    print(f"Max profit will be: {maxProfit}")
    print(f"Job sequence of Execution will be: {jobSequence}")
    endOfExecution=time.time()
    timeRequired.append(round(endOfExecution-startOfExecution,4))
    

    
    
        

