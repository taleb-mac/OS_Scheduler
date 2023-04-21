# OS Scheduler

This is a simple operating system process scheduler built using Python and Tkinter.

## Requirements

- Python 3.x
- Tkinter (included with Python)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<username>/os-scheduler.git
   ```

2. Navigate to the project directory:

   ```bash
   cd os-scheduler
   ```

3. Run the application:

   ```bash
   python app.py
   ```

   **Note**: If you are on macOS, you may need to run the app using the `python` command instead of double-clicking the `os-scheduler.exe` file.

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

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgements

- This project was inspired by the operating system scheduling simulation in the book "Operating System Concepts" by Abraham Silberschatz, Peter B. Galvin, and Greg Gagne.
- The `process_classes.py` module is adapted from a similar module in the "Operating System Concepts" book.

Feel free to modify this template to suit your needs.