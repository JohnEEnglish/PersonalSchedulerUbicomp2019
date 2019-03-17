from Event import Event
from Schedule import Schedule

def receive_and_create_event():
    """
    Receives the input to create an event
    :return:
    """
    created_event = Event()

    # NAME
    while created_event.get_name() == "":
        try:
            event_name = input("What is your event called? ---> ")
            created_event.set_name(event_name)
        except:
            pass
        
    # LOCATION
    while created_event.get_location() == "":
        try:
            event_loc = input("Ok, where is this event located? ---> ")
            created_event.set_location(event_loc)
        except:
            pass        
        
    # DURATION    
    while created_event.get_duration() == -1:
        try:
            event_length = int(input("""
Ok, how long do you expect to be there?: 
    
(Please note this prototype only supports lengths of time comprised of half-hour increments,
up to a maximum value of 48.
For example, if your event will last 1.5 hours, please enter 3). 
---> """))
            assert 0 <= int(event_length) <= 48, "Your event lasts more than a day."
            created_event.set_duration(event_length)
        except:
            pass        
        
    # PRIORITY
    while created_event.get_priority() == 0:
        try:
            event_priority = input("""                               
Please enter a "priority factor" from the options below:
    0 - Use Default Prioritization
    1 - Est. Traffic Conditions
    2 - Weather
    3 - Est. Driving Time
    4 - Destination Popularity
    5 - Est. Wait Time
    
    Your selection: """)
            if int(event_priority) in created_event.priority_dict:
                created_event.set_priority(int(event_priority))
#                created_event.display_event_priority()
                break
            else:
                print("Invalid Selection.")
        except:
            pass
    return created_event

    # while created_event.get_time() == "-1:00":
    #     try:
    #         event_time = input("Please enter the starting time of your event: ")
    #         assert 0 <= int(event_time[:2]) <= 24, "The hour of your event time is not valid."
    #         assert 0 <= int(event_time[3:5]) <= 59, "The minutes of your event time is not valid."
    #         created_event.set_time(event_time)
    #     except:
    #         pass

def main_interactive_one():
    user_continue = True
    interactive_schedule = Schedule()
    print("""
Hello and welcome to the Personal Scheduling Assistant (P.S.A.).

This system will recommend the best time for you to schedule
a new event, based on a variety of factors.
    """)
    while user_continue:
        user_event = receive_and_create_event()
        interactive_schedule.add_event(user_event)
        user_continue = False
#        print("Would you like to add another event?")
#        prompt_continue = None
#        while prompt_continue is None:
#            try:
#                yes_no = input("(yes/no) ")
#                if yes_no.lower() == "yes":
#                    user_continue = True
#                elif yes_no.lower() == "no":
#                    user_continue = False
#                else:
#                    user_continue = None
#                prompt_continue = user_continue
#            except:
#                pass
    interactive_schedule.display_schedule()
    interactive_schedule.display_recommendation(user_event.get_name())


def main_one():
    event_one = Event(1, name="Tennis")
    event_two = Event(2, name="Scuba Diving")
    schedule_main_one = Schedule()
    schedule_main_one.add_event(event_one)
    schedule_main_one.display_recommendation("Tennis")
    schedule_main_one.add_event(event_two)
    # schedule_main_one.display_schedule()


if __name__ == "__main__":
#    main_one()
    main_interactive_one()
