import pyautogui
import time

# Time interval in seconds
interval = 33
progress_bar_length = 33  # Length of the progress bar (in characters)

def change_song():
    # pyautogui.hotkey('command', '1')    # Assumes Spotify is the first tab
    # time.sleep(0.5)  # Small delay to ensure the tab is active

    # Simulate the "Next" button press
    pyautogui.hotkey('option', 'right')

# Main loop
i = 0
try:
    while True:
        for j in range(interval):
            # Print progress bar
            progress = int((j + 1) / interval * progress_bar_length)
            print(f"\rProgress: [{'#' * progress}{'.' * (progress_bar_length - progress)}] {j + 1}/{interval} sec", end='')
            time.sleep(1)
        
        change_song()
        print(f"\nChanging song: {i}")
        i += 1
except KeyboardInterrupt:
    print("\nScript stopped manually.")
