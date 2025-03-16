import time

def start_countdown():
    """Ask the user for countdown time and start the countdown."""
    try:
        seconds = int(input("Enter countdown time in seconds: "))  # Get user input
        while seconds:
            minutes, sec = divmod(seconds, 60)
            time_format = f"{minutes:02d}:{sec:02d}"
            print(f"Time left: {time_format}", end="\r")
            time.sleep(1)
            seconds -= 1
        
        print("\nTime's up! Attention!")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Example usage
start_countdown()