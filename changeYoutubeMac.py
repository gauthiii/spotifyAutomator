import pyautogui
import time
from datetime import datetime

# Time interval in seconds
interval = 33
progress_bar_length = 33  # Length of the progress bar (in characters)

def change_song():
    # Simulate pressing the 'j' key for YouTube Music
    pyautogui.press('j')

# Main loop
i = 0
st = datetime.now()
startTime = st.strftime("%d/%m/%Y %H:%M:%S")
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
    et = datetime.now()
    endTime = et.strftime("%d/%m/%Y %H:%M:%S")
    difference = et - st

    print("\nScript stopped manually.")
    print("\nStarting Date and time =", startTime)
    print("Completed Date and time =", endTime)
    print("Code ran for:", difference)
