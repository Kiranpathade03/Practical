# Q2) Write a Python program to solve water jug problem.
# Two jugs with capacity 4 gallon and 3 gallon are given with unlimited water supply.
# Target: Achieve exactly 2 gallons of water in the second jug.
# Written by: (Your Name)

from collections import deque

start = (0, 0)  # (Jug A: 4 gallons, Jug B: 3 gallons)
goal = 2

visited = set()
queue = deque([start])

print("\n--- Water Jug Result Steps ---")

while queue:
    a, b = queue.popleft()
    print(f"Current State: ({a}, {b})")

    if b == goal:
        print("\nGoal Achieved ✓ Final State:", (a, b))
        break

    visited.add((a, b))

    moves = [
        (4, b),  # Fill Jug A
        (a, 3),  # Fill Jug B
        (0, b),  # Empty Jug A
        (a, 0),  # Empty Jug B
        (max(0, a - (3 - b)), min(3, b + a)),  # Pour A → B
        (min(4, a + b), max(0, b - (4 - a)))   # Pour B → A
    ]

    for state in moves:
        if state not in visited:
            queue.append(state)
