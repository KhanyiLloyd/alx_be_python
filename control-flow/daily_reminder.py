# Ask the user to enter task description
task= input("Enter your task: ")
priority= input("What is the task's priority level? (high, medium, low: ")
time_bound= input ("Is the task time-bound? (yes,no): ")

#Executing the code

match priority:
  case "high":
    reminder= f"Reminder: {task} is a high priority task"
    if time_bound == "yes":
       reminder += " that requires immediate attention today!"
    print(reminder)

  case "medium":
    reminder= f"Note: {task} is a medium priority task"
    if time_bound == "yes":
       reminder += " that requires immediate attention today!"
    print(reminder)

  case "low":
    reminder= f"Note: {task} is a low priority task."
    if time_bound == "yes":
       reminder += " that requires immediate attention today!"
    else:
       reminder += " Consider completing it when you have free time."
    print(reminder)