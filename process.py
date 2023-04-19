class Process:
    def __init__(self, pid, arrival_time, priority, burst_time=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.finish_time = None
        
    def __str__(self):
        return f'''
        Process: {self.pid}
        Priority: {self.priority}
        Arrival time: {self.arrival_time}
        Burst time: {self.burst_time}
        Finish time: {self.finish_time}'''
