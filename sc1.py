# import pyautogui
# import time

# def simulate_key_press(key, interval):
#     """
#     Simulate a key press at regular intervals.

#     Args:
#     key (str): The key to press.
#     interval (int): The time interval (in seconds) between key presses.
#     """
#     print(f"Starting key press simulation for '{key}' every {interval} seconds. Press Ctrl+C to stop.")
#     try:
#         while True:
#             pyautogui.press(key)
#             print(f"Key '{key}' pressed.")
#             time.sleep(interval)
#     except KeyboardInterrupt:
#         print("\nStopped key press simulation.")

# if __name__ == "__main__":
#     key_to_press = "a"  # Change to the desired key
#     time_interval = 5  # Change to the desired interval (in seconds)
#     simulate_key_press(key_to_press, time_interval)


import pyautogui
import time

def simulate_separate_key_presses(keys, interval):
    """
    Simulate separate key presses at regular intervals.

    Args:
    keys (list): List of keys to press one by one.
    interval (int): The time interval (in seconds) between key presses.
    """
    # print(f"Starting separate key presses simulation for {keys} every {interval} seconds. Press Ctrl+C to stop.")
    try:
        while True:
            for key in keys:
                pyautogui.press(key)
                # print(f"Key '{key}' pressed.")
                print('k')
                time.sleep(1)  # Add a delay between individual key presses
            time.sleep(interval - len(keys))  # Adjust interval for total time
    except KeyboardInterrupt:
        print("\nStopped key press simulation.")

if __name__ == "__main__":
    keys_to_press = ["ctrl", "shift"]  # Keys to press separately
    time_interval = 5  # Total interval between cycles
    simulate_separate_key_presses(keys_to_press, time_interval)
