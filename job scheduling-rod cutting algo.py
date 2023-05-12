


def job_scheduling(jobs):
  """
  This function finds the maximum profit that can be made by scheduling jobs in non-overlapping way.

  Args:
    jobs: A list of jobs, where each job is a tuple of (name, deadline, profit).

  Returns:
    The maximum profit that can be made by scheduling jobs.
  """

  # Create a table to store the maximum profit that can be made by scheduling up to a given deadline.
  profit_table = [[0 for _ in range(len(jobs))] for _ in range(len(jobs))]

  # Initialize the profit table.
  for i in range(len(jobs)):
    profit_table[i][i] = jobs[i][2]

  # Fill in the profit table.
  for i in range(len(jobs) - 1, -1, -1):
    for j in range(i + 1, len(jobs)):
      if jobs[i][1] <= jobs[j][1]:
        profit_table[i][j] = max(profit_table[i][j - 1], profit_table[i + 1][j] + jobs[i][2])

  # Initialize the output list.
  output = []

  # Iterate over the profit table from the last row to the first row.
  for i in range(len(jobs) - 1, -1, -1):
    # If the current row has a higher profit than the previous row, then add the job at the current row to the output list.
    if profit_table[i][-1] >= profit_table[i + 1][-1]:
      output.append(jobs[i])

  # Reverse the output list.
  output.reverse()

  # Return the output list.
  return output

jobs = [("Job A", 2, 6), ("Job B", 6, 4), ("Job C", 7, 2), ("Job D", 1, 5), ("Job E", 5, 11)]

print(job_scheduling(jobs))