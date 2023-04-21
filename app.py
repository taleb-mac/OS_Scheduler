import tkinter as tk
from tkinter import filedialog
from scheduler import scheduler, read_file, calculate_times
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def open_file():
    file_name = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_name:
        processes = read_file(file_name)
        gantt_chart = scheduler(processes)
        calculate_times(processes)
        
        output = "Gantt Chart:\n" + gantt_chart +  "\nProcess Information:\n"
        for process in processes:
            output += f"{process.pid}:\n"
            output += f"  Turnaround Time: {process.turnaround_time}\n"
            output += f"  Response Time: {process.response_time}\n"
            output += f"  Waiting Time: {process.waiting_time}\n"

        txt_output.config(state=tk.NORMAL)  # Enable editing before inserting the output
        txt_output.delete(1.0, tk.END)
        txt_output.insert(tk.END, output)
        txt_output.config(state=tk.DISABLED)  # Disable editing after inserting the output


root = tk.Tk()
root.title("Scheduler GUI")
root.geometry("800x600")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

txt_output = tk.Text(frame, wrap=tk.WORD, font=("Arial", 12))
txt_output.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

scroll_bar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=txt_output.yview)
scroll_bar.grid(column=1, row=0, sticky=(tk.N, tk.S))
txt_output["yscrollcommand"] = scroll_bar.set

frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

btn_open = ttk.Button(root, text="Open File", command=open_file)
btn_open.grid(column=0, row=1, pady=10)

root.mainloop()
