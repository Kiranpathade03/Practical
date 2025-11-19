# Q1) Write a Python program using Means-End Analysis algorithm to transform a string.
# Program: Transform a lowercase string into another using Means-End Analysis
# Written by: (Your Name)

start = input("Enter the start string: ")
goal = input("Enter the goal string: ")

current = start
step = 1

print("\n--- Means-End Analysis Process ---")

while current != goal:

    # If strings are same length, replace mismatching character
    if len(current) == len(goal):
        for i in range(len(current)):
            if current[i] != goal[i]:
                current = current[:i] + goal[i] + current[i+1:]
                print(f"Step {step}: Substitute -> {current}")
                break

    # If current string is shorter, insert missing character
    elif len(current) < len(goal):
        current += goal[len(current)]
        print(f"Step {step}: Insert -> {current}")

    # If current string is longer, delete character
    else:
        current = current[:-1]
        print(f"Step {step}: Delete -> {current}")

    step += 1

print("\nFinal Result:", current)
print("Goal Reached ✓")
