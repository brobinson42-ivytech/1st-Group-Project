while True:
 try:
  hours_worked = float(input("How many hours did you work this week?"))
  if hours_worked < 0:
   print("Hours worked cannot be negative. Please enter a valid number.")
  else:
   break
 except: ValueError
 print("Why you putting letters? You crazy. Numbers only, son")
if hours_worked <= 40:
 gross = hours_worked * 29.28
 print(f"You made ${gross:.2f} this week")
else:
    gross = 40 * 29.28
    over = hours_worked - 40
    overtime = over * (29.28 * 1.5)
    gross = gross + overtime
    print(f"You made ${gross:.2f} this week")
input("Press enter to continue")
