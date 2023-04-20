class Process:
    def __init__(self, pid, arrival_time, priority, burst_time=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.finish_time = None
        self.start_time = None
        self.turnaround_time = None
        self.response_time = None
        self.waiting_time = None
        
    def __str__(self):
        return f'''
        Process: {self.pid}
        Priority: {self.priority}
        Arrival time: {self.arrival_time}
        Burst time: {self.burst_time}
        Finish time: {self.finish_time}'''


class Execution:
    def __init__(self, pid, start_time, end_time, curr_queue):
        self.pid = pid
        self.start_time = start_time
        self.end_time = end_time
        self.current_queue = curr_queue

    def __str__(self):
        return f"{self.pid} ({self.start_time}-{self.end_time}) - {self.current_queue}"