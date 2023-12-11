import time

def format_execution_time(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    if hours > 0:
        return f"{hours} hours, {minutes} minutes and {seconds} seconds"
    elif minutes > 0:
        return f"{minutes} minutes and {seconds} seconds"
    elif seconds > 0:
        return f"{seconds} seconds"
    else:
        return f"less than a second"

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = time.monotonic()
        result = func(*args, **kwargs)
        final_time = time.monotonic()
        execution_time = final_time - initial_time
        formatted_time = format_execution_time(execution_time)
        print(f"Execution time: {formatted_time}.")
        return result
    return wrapper