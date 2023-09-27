""" # Starting a car
action = ""
while action != "quit":
  print('Start car')
  action= input("Start the car").lower()
if action == start:
  print("Car started ... Ready to go!")
else:
  print('Car not started') """
  
command = ""
while command.lower() != "quit":
  command = input("> ").lower()
  if command == "start":
    print("car started")
  elif command == "stop":
    print("car stopped")
  elif command == "help":
    print("""
          start - to start the car
          stop - to stop the car
          quit - to quit
          """)
  else:
    print("Sorry, I dont understand that command")