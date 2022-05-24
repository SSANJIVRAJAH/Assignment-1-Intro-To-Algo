def queue_system():
    queue = []
    ticket_number = 1001
    counter1 = []
    counter2 = []
    counter3 = []
    counter4 = []
    counter_list = [counter1, counter2, counter3, counter4]
    counter_status = ['Not Assigned', 'Not Assigned', 'Not Assigned', 'Not Assigned']
    print("""Enter 0 to 5 for the following options:
0 -> Issue new ticket number
1 -> Assign first ticket in queue to Counter 1
2 -> Assign first ticket in queue to Counter 2
3 -> Assign first ticket in queue to Counter 3
4 -> Assign first ticket in queue to Counter 4
5 -> Quit program""")
    print()

    while True:
        try:
            choice = int(input("Enter your options: "))
        except ValueError:
            print("Please enter a number between 0 and 5 asshole.")
            continue
        if choice == 0:  # Issue new ticket number
            print(f"New ticket number: {ticket_number}")  # New ticket number
            queue.append(ticket_number)  # Append ticket number to queue
            ticket_number += 1  # Increment ticket number by 1
        elif choice == 1:  # Assign first ticket in queue to Counter 1
            if len(queue) != 0:  # if queue is not empty
                if counter_status[0] == 'Not Assigned':  # if counter is empty
                    counter_status[0] = queue[0]  # counter is now occupied
                    counter1.append(queue[0])  # Assign first ticket in queue to counter 1
                    queue.remove(queue[0])  # Remove first ticket in queue
                else:
                    print("Counter 1 is busy.")  # If counter 1 is busy, print message
            else:
                print("Queue is empty.")  # If queue is empty, print message
        elif choice == 2:
            if len(queue) != 0:
                if counter_status[1] == 'Not Assigned':
                    counter_status[1] = queue[0]
                    counter2.append(queue[0])
                    queue.remove(queue[0])
                else:
                    print("Counter 2 is busy.")
            else:
                print("Queue is empty.")
        elif choice == 3:
            if len(queue) != 0:
                if counter_status[2] == 'Not Assigned':
                    counter_status[2] = queue[0]
                    counter3.append(queue[0])
                    queue.remove(queue[0])
                else:
                    print("Counter 3 is busy.")
            else:
                print("Queue is empty.")
        elif choice == 4:
            if len(queue) != 0:
                if counter_status[3] == 'Not Assigned':
                    counter_status[3] = queue[0]
                    counter4.append(queue[0])
                    queue.remove(queue[0])
                else:
                    print("Counter 4 is busy.")
            else:
                print("Queue is empty.")
        elif choice == 5:
            print("Quitting program...")
            break
        else:
            print("Invalid option, try again...")
        print(f"Tickets in queue: {queue}")
        # print(f"Counter 1: {counter1}")
        # print(f"Counter 2: {counter2}")
        # print(f"Counter 3: {counter3}")
        # print(f"Counter 4: {counter4}")
        # print(f"Counter Status: {counter_status}")
        # print(f"Counter Assignment: {counter_list}")
        print(f"Counter Assignment: {{'Counter 1':'{counter_status[0]}', 'Counter 2': '{counter_status[1]}',"
              f" 'Counter 3': '{counter_status[2]}', "f"'Counter 4': '{counter_status[3]}'}}")
        print()


queue_system()

