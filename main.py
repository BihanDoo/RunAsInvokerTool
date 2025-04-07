import customtkinter as ctk
import subprocess
import os
from tkinter import filedialog

# Initialize the app
ctk.set_appearance_mode("System")  # "Dark", "Light", or "System"
ctk.set_default_color_theme("blue")  # Theme: "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("Run EXE as Invoker")
app.geometry("500x200")

selected_exe_path = ctk.StringVar()

def browse_exe():
    filepath = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
    if filepath:
        selected_exe_path.set(filepath)

def run_as_invoker():
    exe_path = selected_exe_path.get()
    if not exe_path:
        result_label.configure(text="Please select an .exe file first.")
        return

    env = os.environ.copy()
    env["__COMPAT_LAYER"] = "RunAsInvoker"

    try:
        subprocess.run([exe_path], env=env, check=True)
        result_label.configure(text="Executed successfully.")
    except subprocess.CalledProcessError as e:
        result_label.configure(text=f"Execution failed. Code: {e.returncode}")
    except Exception as e:
        result_label.configure(text=f"Error: {e}")

# UI Components
browse_button = ctk.CTkButton(app, text="Browse .exe", command=browse_exe)
browse_button.pack(pady=10)

path_label = ctk.CTkLabel(app, textvariable=selected_exe_path, wraplength=450)
path_label.pack(pady=5)

run_button = ctk.CTkButton(app, text="Run as Invoker", command=run_as_invoker)
run_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", text_color="gray")
result_label.pack(pady=5)

yeeyeeahhlabel = ctk.CTkLabel(app, text="yeeyeeass tool made by BihanDoo!!!", text_color="blue")
yeeyeeahhlabel.pack(pady=5)

# Start the app
app.mainloop()
