"""Run an infinite loop that prints an iteration counter once per second.

This module loops forever, printing a short message on each iteration, and
only stops when the user interrupts it with Ctrl+C (KeyboardInterrupt), at
which point it prints a goodbye message and exits cleanly.
"""

import time


def main():
    """Loop forever, printing an iteration counter until interrupted."""
    counter = 0
    try:
        while True:
            counter += 1
            print(f"Iteration {counter}: still looping, press Ctrl+C to stop.")
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\nInterrupted after {counter} iteration(s). Goodbye!")


if __name__ == "__main__":
    main()
