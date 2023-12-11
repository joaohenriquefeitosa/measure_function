# Execution Time Decorator

## Purpose

The `measure_execution_time` decorator is designed to measure and print the execution time of any function in a human-readable format. It is useful for performance testing and optimization.

## How to Use

To use the `measure_execution_time` decorator, follow these steps:

1. Import the decorator from the `timing_decorator.py` file:

```
from timing_decorator import measure_execution_time
```

2. Apply the `@measure_execution_time` decorator to any function you want to measure:

```
@measure_execution_time
def function_to_measure():
    # Function code
```

3. Run your function as usual, and the execution time will be printed to the console.

## Output Format

The decorator will print the execution time in a human-friendly format:
- If the execution time is less than a minute, it will print in seconds (e.g., "Execution time: 12 seconds.").
- If the execution time is more than a minute, it will print in minutes and seconds (e.g., "Execution time: 2 minutes and 5 seconds.").
- If the execution time is more than an hour, it will include hours (e.g., "Execution time: 1 hour, 15 minutes and 30 seconds.").