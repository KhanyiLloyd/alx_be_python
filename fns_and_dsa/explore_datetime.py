from datetime import datetime, timedelta
def display_current_datetime():
  """ 
  Retrieves the current date and time and 
  formats it in YYY-MM_DD HH:MM:SS
  """
  current_date=datetime.now()
  formatted_current_date=current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted_current_date}")

  def calculate_future_date():
    """ 
    Asks the user for a number of days
    calculates a future date by adding the days to the current date
    prints the future date in YYY-MM_DD
    """
  while True:
    days_to_add_str= input("Enter the number of days to add to the current date: ")
    if days_to_add_str.isdigit():
      days_to_add = int(days_to_add_str)
      break
    else:
      print("Invalid input. Please enter a whole number (digits) for the number of days")
    
    current_date_for_future_cal=datetime.now()
    time_delta=timedelta(days=days_to_add)
    future_date=current_date_for_future_cal + time_delta
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

    if __name__ == "__main__":
      display_current_datetime()
      calculate_future_date()