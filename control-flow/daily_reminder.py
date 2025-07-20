#Ask the user to enter task description
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

#Executing the code

match priority:
  case "high":
    task_reminder= f" '{task}' is a high priority task."
    if time_bound == "yes":
      print(f"Reminder: {task_reminder} that requires immediate attention today!")
    else:
     print(f"Reminder: {task_reminder}")


  case "medium":
    task_reminder= f" '{task}' is a medium priority task."
    if time_bound == "yes":
       print(f"Note: {task_reminder} that requires immediate attention today!")
    else:
      print(f"Note: {task_reminder}")

  case "low":
    task_reminder= f" '{task}' is a low priority task."
    if time_bound == "yes":
       print(f"Note: {task_reminder} that requires immediate attention today!")
    elif time_bound == "no":
       print(f"Note: {task_reminder} Consider completing it when you have free time.")
    else:
      print(f"Note: {task_reminder}")