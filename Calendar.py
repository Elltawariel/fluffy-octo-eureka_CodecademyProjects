""" 
Hello
I am Anastasiia's program
Good Luck
"""

from time import sleep, strftime
name = "Anastasiia"
print "Hello %s" % (name)
calendar = {}
def welcome():
  print "Welcome" + str(name)
  print "Calendar is opening..."
  sleep(1)
  print "Today is " + str(strftime("%A, %B, %d, %Y"))
  print "Time is " + str(strftime("%H, %M, %S"))
  sleep(1)
  print "What would you like to do?"
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) == 0:
        print "Calendar is empty"
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update successful"
      print calendar
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
          print "Incorrect Value"
          try_again = raw_input("Try Again? Y for Yes, N for No: ")
          try_again = try_again.upper()
          if try_again == "Y":
            continue
          else:
            start = False
      else:
        calendar[date] = event
        print "Success"
    elif user_choice == "D":
      if len(calendar.keys()) == 0:
        print "Empty calendar"
      else:
        event = raw_input("Enter event: ")
        for date in calendar.keys():
          if calendar[date] == event:
            del calendar[date]
            print "Delete Success"
            print calendar
          else:
            print "Event not found"
    elif user_choice == "X":
      start = False
    else:
      print "Invalid command"
      start = False

start_calendar()






    

    
    
