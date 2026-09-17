import csv
from pynput import keyboard

reset_sequence = {
    keyboard.KeyCode.from_char('x'),
    keyboard.KeyCode.from_char('z'),
    keyboard.Key.backspace,
    keyboard.Key.enter,
}

key_buffer = set()


def on_press(key):
    global key_buffer
    if key in reset_sequence and key not in key_buffer:
        key_buffer.add(key)

    if key_buffer == reset_sequence:
        with open('counter.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            counter = int(next(reader)[0])  # Read the current counter value

        counter += 1  # Increment the counter

        with open('counter.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Counter']) # Writes the header row
            writer.writerow([counter])  # Write the updated counter value

        key_buffer.clear()  # Clear the buffer after resetting the counter


    elif key == keyboard.Key.esc:
        return False  # Exit the program when escape is pressed

def on_release(key):
    global key_buffer
    if key in key_buffer:
        key_buffer.discard(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()