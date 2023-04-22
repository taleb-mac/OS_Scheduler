# OS Scheduler

A Four-Level Priority Scheduler (simulator) using Python, managing processes across Real-Time and three user priority levels. The scheduler uses a First Come First Served (FCFS) approach for Real-Time processes, while normal user processes employ a three-level feedback queue. The report covers the key components, input and output, and main scheduling functions, showcasing the scheduler's effective prioritization and performance.


## Requirements

- Python 3.x
- Tkinter (included with Python)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/taleb-mac/OS_Scheduler.git
   ```

2. Navigate to the `OS_Scheduler/` directory:

   ```
   OS_Scheduler/
   ├── dist/
   │   └── app.exe
   ├── process_classes.py
   ├── scheduler.py
   ├── README.md
   └── app.py
   ```

3. Run the application:

   - **Windows**: double-click the `app.exe` file under dist/.
   - **macOS**: open a terminal window, navigate to the project directory, and run the following command:

     ```bash
     python app.py
     ```

## Usage

1. Click the "Open File" button to select a text file containing process information.
2. The application will calculate the schedule and display the Gantt chart and process information in the output text area.

## File Format

The input text file should contain one process per line in the following format:

```
arrival_time,priority,burst_time
```

- `arrival_time`: the time at which the process arrives (integer)
- `priority`: the priority of the process (integer, 0-3)
- `burst_time`: the time required for the process to complete (integer)

Here is an example input file:

```
0,0,10
1,1,5
2,2,3
3,3,2
```
