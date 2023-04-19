from process import Process


def read_file(file_name):
    # Read the file and return a list of processes
    processes = []
    with open(file_name, 'r') as f:
        for index, line in enumerate(f):
            arrival_time, priority, burst_time = line.split(',')
            processes.append(Process(f'P{index}', int(arrival_time), int(priority), int(burst_time)))
    return processes

def first_comes_first_served(process, time):
    # For real time queue
    time += process.burst_time
    process.finish_time = time
    process.remaining_time = 0
    print(f'Process {process.pid} finished at {time}.')
    return time

def round_robin(process, q, time):
    # For user job queue
    if process.remaining_time - q <= 0:
        time += process.remaining_time
        process.remaining_time = 0
    else:
        time += q
        process.remaining_time -= q
    
    return time

def check_preempt(processes, quantum, time):
    # Check if any priority 0 processes will arive in the next time slice
    try:
        process = min([process for process in processes if process.arrival_time <= time + quantum and process.priority == 0], key=lambda x: x.arrival_time)
    except:
        return False
    else:
        return process.arrival_time - time

def scheduler(processes, time=0):
    while True:
        # Check if all processes are finished and break the loop
        if all([True if process.remaining_time == 0 else False for process in processes]):
            break
        
        # Get the real time queue sort it by arrival time then execute using first_comes_first_served
        real_time_queue = [process for process in processes if process.arrival_time <= time and process.remaining_time and process.priority == 0]
        if real_time_queue:
            process = min(real_time_queue, key=lambda x: x.arrival_time)
            time = first_comes_first_served(process, time)
            continue
        
        # Get the user job queue (priority 1) sort it by arrival time then execute one time slice using round_robin
        priority_1_queue = [process for process in processes if process.arrival_time <= time and process.remaining_time and process.priority == 1]
        if priority_1_queue:
            process = min(priority_1_queue, key=lambda x: x.arrival_time)
            time = round_robin(process, 1, time)
            process.priority += 1
            continue
        
        # Preempt the process if there is a priority 0 process that will arrive in the next time slice
        quantum = 1 if check_preempt(processes, 2, time) else 2
        
        # Get the user job queue (priority 2) sort it by arrival time then execute one time slice using round_robin
        priority_2_queue = [process for process in processes if process.arrival_time <= time and process.remaining_time and process.priority == 2]
        if priority_2_queue:
            process = min(priority_2_queue, key=lambda x: x.arrival_time)
            time = round_robin(process, quantum, time)
            process.priority += 1
            continue
        
        # Preempt the process if there is a priority 0 process that will arrive in the next time slice
        if q:= check_preempt(processes, 4, time): quantum = q
        else: quantum = 4

p = read_file('processes.txt')
scheduler(p)
        
        
        
        
        
        
        

        
        

        
               


        
        
        
        
        
        