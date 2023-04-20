from process_classes import Process, Execution


def read_file(file_name):
    # Read the file and return a list of processes
    processes = []
    with open(file_name, 'r') as f:
        for index, line in enumerate(f):
            arrival_time, priority, burst_time = line.split(',')
            processes.append(Process(f'P{index}', int(arrival_time), int(priority), int(burst_time)))
    return processes

def calculate_times(processes):
    for process in processes:
        process.turnaround_time = process.finish_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

def print_gantt_chart(executions):
    print("Gantt Chart:")
    for execution in executions:
        print(execution)

def first_comes_first_served(process, time):
    # For real time queue
    if process.start_time is None:
        process.start_time = time
        process.response_time = time - process.arrival_time
    time += process.burst_time
    process.finish_time = time
    process.remaining_time = 0
    return time

def round_robin(process, q, time):
    # For user job queue
    if process.start_time is None:
        process.start_time = time
        process.response_time = time - process.arrival_time
    if process.remaining_time - q <= 0:
        time += process.remaining_time
        process.remaining_time = 0
        process.finish_time = time
    else:
        time += q
        process.remaining_time -= q

    return time

def check_preempt(processes, quantum, time):
    # Check if any priority 0 processes will arrive in the next time slice
    future_priority_0_processes = [process for process in processes if process.arrival_time > time and process.priority == 0]
    
    if not future_priority_0_processes:
        return False

    next_priority_0_process = min(future_priority_0_processes, key=lambda x: x.arrival_time)
    time_till_next_priority_0_process = next_priority_0_process.arrival_time - time

    if time_till_next_priority_0_process < quantum:
        return time_till_next_priority_0_process
    else:
        return False

def scheduler(processes, time=0):
    # initialize the queues
    priority_3_queue = []
    executions = [] # keep track of the execution of each process

    while True:
        # Check if all processes are finished and break the loop
        if all([True if process.remaining_time == 0 else False for process in processes]):
            print_gantt_chart(executions)
            print('All processes are finished')
            break

        # Find the next arrival time of the remaining processes
        next_arrival_time = min(
            [process.arrival_time for process in processes if process.remaining_time > 0],
            default=None,
        )

        # If no processes can be executed at the current time, advance the time to the next arrival time
        if next_arrival_time is not None and time < next_arrival_time:
            time = next_arrival_time
        
        # Get the real time queue sort it by arrival time then execute using first_comes_first_served
        real_time_queue = [process for process in processes if process.arrival_time <= time and process.remaining_time > 0 and process.priority == 0]
        if real_time_queue:
            process = min(real_time_queue, key=lambda x: x.arrival_time)
            time = first_comes_first_served(process, time)
            executions.append(Execution(process.pid, time - process.burst_time, time, 'Real Time'))
            continue

        quantum = 1
        # Get the user job queue (priority 1) sort it by arrival time then execute one time slice using round_robin
        priority_1_queue = [process for process in processes if process.arrival_time <= time and process.remaining_time > 0 and process.priority == 1]
        if priority_1_queue:
            process = min(priority_1_queue, key=lambda x: x.arrival_time)
            prev_time = time
            time = round_robin(process, quantum, time)
            executions.append(Execution(process.pid, prev_time, time, 'User Job - Priority 1'))
            process.priority += 1
            continue
        
        # Preempt the process if there is a priority 0 process that will arrive in the next time slice
        quantum = 1 if check_preempt(processes, 2, time) is not False else 2
        
        # Get the user job queue (priority 2) sort it by arrival time then execute one time slice using round_robin
        priority_2_queue = [process for process in processes if process.arrival_time <= time and process.remaining_time > 0 and process.priority == 2]
        if priority_2_queue:
            process = min(priority_2_queue, key=lambda x: x.arrival_time)
            prev_time = time
            time = round_robin(process, quantum, time)
            executions.append(Execution(process.pid, prev_time, time, 'User Job - Priority 2'))
            process.priority += 1
            continue
        
        # Preempt the process if there is a priority 0 process that will arrive in the next time slice
        if (q:= check_preempt(processes, 4, time)) is not False: quantum = q
        else: quantum = 4
        
        # Get the user job queue (priority 3) sort it by arrival time then execute one time slice using round_robin
        if not priority_3_queue:
            priority_3_queue = [process for process in processes if process.arrival_time <= time and process.remaining_time > 0 and process.priority == 3]
        else:
            priority_3_queue += sorted([process for process in processes if process.arrival_time <= time and process.remaining_time > 0 and process.priority == 3 and process not in priority_3_queue], key=lambda x: x.arrival_time)      
        
        if priority_3_queue:
            process = priority_3_queue.pop(0)
            prev_time = time
            time = round_robin(process, quantum, time)
            if process.remaining_time: 
                priority_3_queue.append(process)
            executions.append(Execution(process.pid, prev_time, time, 'User Job - Priority 3'))
            continue





def main():
    processes = read_file('processes.txt')
    scheduler(processes)
    calculate_times(processes)

    print("\nProcess Information:")
    for process in processes:
        print(f"{process.pid}:")
        print(f"  Turnaround Time: {process.turnaround_time}")
        print(f"  Response Time: {process.response_time}")
        print(f"  Waiting Time: {process.waiting_time}")

if __name__ == "__main__":
    main()