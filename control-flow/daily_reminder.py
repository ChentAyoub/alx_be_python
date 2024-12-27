task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority == "high":
    reminder = f"Reminder: '{task}' is a high priority task"
elif priority == "medium":
    reminder = f"Reminder: '{task}' is a medium priority task"
elif priority == "low":
    reminder = f"Reminder: '{task}' is a low priority task"
else:
    reminder = "Invalid priority level entered."

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
else:
    reminder += ". However, the time-bound information entered is invalid."

print(reminder)
