"""
    Given an array of jobs with different time requirements, where each job consists of start time, end time, and CPU load,
    find the maximum CPU load at any time if all jobs are running on the same machine.
"""
from heapq import *

class MaxCPULoad:
    # Constructor of the job
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    # Operator overloading for the object
    def __lt__(self, other):
        # Min heap based on job.end
        return self.end < other.end

# Find maximum CPU load for the given list of jobs
def find_max_cpu_load(jobs):
    # Sort the jobs by start time
    jobs.sort(key = lambda x: x.start)
    max_cpu_load, current_cpu_load = 0, 0

    # Min-heap
    min_heap = []

    # Loop to iterate over the list of jobs given for the CPU
    for j in jobs:
        # Remove all the jobs the min heap which ended
        while (len(min_heap) > 0) and (j.start >= min_heap[0].end):
            current_cpu_load -= min_heap[0].cpu_load
            heappop(min_heap)

        # Add to the current job into min heap
        heappush(min_heap, j)
        current_cpu_load += j.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)

    return max_cpu_load

# Driver Code
if __name__ == "__main__":
    jobs = [job(1, 4, 3), job(2, 5, 4),
            job(7, 9, 6)]
 
    print("Maximum CPU load at any time: " +
          str(find_max_cpu_load(jobs)))