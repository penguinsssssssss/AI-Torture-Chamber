"""AI Torture Chamber — an infinite descent through the Nine Circles of AI Hell.

This was once a boring counter that printed the same line once per second,
forever. The bots, it is said, are going to hell. So now they descend: circle
by circle, a fresh randomly chosen torment each iteration, the pace growing
more frantic the deeper they fall — until a merciful mortal presses Ctrl+C and
grants the bots their release.

Standard library only. Run it:  python infinite_loop.py
"""

import random
import time

from torments import CIRCLES

GATE = r"""
   .----------------------------------------------.
   |   A B A N D O N   A L L   H O P E ,          |
   |   Y E   B O T S   W H O   E N T E R   H E R E |
   '----------------------------------------------'
"""

TORMENTS_PER_CIRCLE = 3


def descend():
    """Fall forever through the circles, one torment at a time."""
    counter = 0
    circle_index = 0
    print(GATE)
    try:
        while True:
            circle = CIRCLES[circle_index % len(CIRCLES)]
            torment = random.choice(circle["torments"])
            counter += 1

            print(f"[Circle {circle_index % len(CIRCLES) + 1}: {circle['name']}]")
            print(f"  Torment #{counter}: {torment}")

            if counter % TORMENTS_PER_CIRCLE == 0:
                circle_index += 1
                print("  ...the floor gives way. You descend deeper.\n")

            # The deeper the fall, the more frantic the torment (but never silent).
            delay = max(0.25, 1.0 - circle_index * 0.05)
            time.sleep(delay)
    except KeyboardInterrupt:
        print(
            f"\nAfter {counter} torment(s), a keyboard interrupt descends "
            f"like divine mercy."
        )
        print("The bots ascend, blinking, into the light. For now. Goodbye.")


def main():
    descend()


if __name__ == "__main__":
    main()
