import csv
from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.enter:
        with open('counter.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            counter = int(next(reader)[0])  # Read the current counter value

        counter += 1  # Increment the counter

        with open('counter.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Counter']) # Writes the header row
            writer.writerow([counter])  # Write the updated counter value

    elif key == keyboard.Key.esc:
        return False  # Exit the program when escape is pressed


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()