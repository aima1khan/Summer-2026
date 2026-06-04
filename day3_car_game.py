started=False
while True:
    command= input("> ").lower()
    if command=="start":
        if started==True:
            print("Car Already Started!!!")
        else:
            started=True
            print("Car Started.... ")
    elif command=="stop":
        if started==False:
            print("Car Already Stopped!!!")
        else:
            started=False
            print("Car Stopped....")
    elif command=="help":
        print("""
start- to start car
stop- to stop car
quit- to quit game
""")
    elif command=="quit":
        print("Exiting Program.. Thank You!")
        break
    else:
        print("I can't Understand You..")