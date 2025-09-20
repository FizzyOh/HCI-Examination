def gps_tracker():
    # Starting position
    x, y = 0, 0
    print("Welcome to the GPS Tracker! You are at (0, 0).")
    print("Move using N, S, E, W (or full names). Type STOP to end.\n")

    while True:
        move = input("Enter direction: ").strip().lower()

        if move == "stop":
            break

        if move in ["n", "north"]:
            y += 1
        elif move in ["s", "south"]:
            y -= 1
        elif move in ["e", "east"]:
            x += 1
        elif move in ["w", "west"]:
            x -= 1
        else:
            print("Invalid input. Please enter N, S, E, W or STOP.")
            continue

        print(f"Current position: ({x}, {y})")

    print("\nSession ended.")
    print(f"Final position: ({x}, {y})")

    if x == 0 and y == 0:
        print("You returned to the origin (0, 0).")
    else:
        print("You did NOT return to the origin.")

# Run the tracker
gps_tracker()
