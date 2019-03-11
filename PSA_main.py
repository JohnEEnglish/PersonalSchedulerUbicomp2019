from Event import Event
from Schedule import Schedule


def receive_and_create_event():
    """
    Receives the input to create an event
    :return:
    """
    created_event = Event()

    # TODO Make a function
    while created_event.get_duration() == -1:
        try:
            event_length = int(input("Please enter the length in half hours of your event: "))
            assert 0 <= int(event_length) <= 24, "Your event lasts more than a day."
            created_event.set_duration(event_length)
        except:
            pass

    # TODO Make a function
    # while created_event.get_time() == "-1:00":
    #     try:
    #         event_time = input("Please enter the starting time of your event: ")
    #         assert 0 <= int(event_time[:2]) <= 24, "The hour of your event time is not valid."
    #         assert 0 <= int(event_time[3:5]) <= 59, "The minutes of your event time is not valid."
    #         created_event.set_time(event_time)
    #     except:
    #         pass

    # TODO Make a function
    while created_event.get_name() == "":
        try:
            event_name = input("Please enter the name of your event: ")
            created_event.set_name(event_name)
        except:
            pass

    # TODO Make a function
    while created_event.get_priority() == 0:
        try:
            event_priority = input("""                               
Please enter a "priority factor" from the options below:
    1 - Est. Traffic Conditions
    2 - Weather
    3 - Est. Driving Time
    4 - Destination Popularity
    5 - Est. Wait Time

(To recommend event with default parameters, just press enter) """)
            if event_priority:
                created_event.set_priority(event_priority)
            created_event.display_event_priority()
            break
        except:
            pass
    return created_event


def main_interactive_one():
    user_continue = True
    interactive_schedule = Schedule()
    print("""
Hello and welcome to the Personal Scheduling Assistant.

This system will ask you for a list of events and return a schedule optimized around giving you as much 
free time as possible.
    """)
    while user_continue:
        interactive_schedule.add_event(receive_and_create_event())
        print("Would you like to add another event?")
        prompt_continue = None
        while prompt_continue is None:
            try:
                yes_no = input("(yes/no) ")
                if yes_no.lower() == "yes":
                    user_continue = True
                elif yes_no.lower() == "no":
                    user_continue = False
                else:
                    user_continue = None
                prompt_continue = user_continue
            except:
                pass
    interactive_schedule.display_schedule()


def main_one():
    event_one = Event(1, name="Tennis")
    event_two = Event(2, name="Scuba Diving")
    schedule_main_one = Schedule()
    schedule_main_one.add_event(event_one)
    schedule_main_one.add_event(event_two)
    schedule_main_one.display_schedule()


if __name__ == "__main__":
    main_interactive_one()
