class Schedule:
    """
    This class will hold the schedule for a single day.
    """

    def __init__(self, event_list=[]):
        self.events = event_list
        self.time_slots = []
        self.morning_buffer = 6 # No events will be scheduled prior to this time (6am)
        self.evening_buffer = 21 # No events will be scheduled after this time (10pm)

        time_slot_name_list = self.make_time_slot_name_list()
        for slot in time_slot_name_list:
            self.time_slots.append([slot, "No Event"])

    def update_schedule(self):
        self.events = sorted(self.events, key=lambda x: x.get_priority(), reverse=True)
        for t in self.time_slots:
            t[1] = "No event"
        self.time_slots = self.make_schedule_from_events()

    def make_schedule_from_events(self):
        from copy import deepcopy

        current_time_index = 0
        temp_slots = deepcopy(self.time_slots)
        for event in self.events:
            for time_slice in range(event.get_duration()):
                temp_slots[current_time_index][1] = event.get_name()
                current_time_index += 1
                if time_slice == event.get_duration() - 1:
                    current_time_index = self.travel_offset(time_slots=temp_slots,
                                                            travel_time=2,
                                                            c_t_index=current_time_index)

        return temp_slots

    @staticmethod
    def travel_offset(time_slots=[], travel_time=1, c_t_index=0):
        for x in range(travel_time):
            time_slots[c_t_index][1] = "Traveling"
            c_t_index += 1

        return c_t_index

    def display_schedule(self):
        """
        This prints out the schedule
        :return:
        """
        for slot in self.time_slots:
            print("At time:", slot[0], slot[1], "is scheduled.")
            print("")

    def add_event(self, event):
        """
        This adds an event to the schedule and then updates it
        :param event:  The event to be added to the schedule
        :return:
        """
        self.events.append(event)
        self.update_schedule()

    def make_time_slot_name_list(self):
        time_slot_list = []
        for hour_int in range(self.morning_buffer, self.evening_buffer + 1, 1):
            if hour_int < 10:
                hour = "0" + str(hour_int)
            else:
                hour = str(hour_int)
            time_slot_list.append(hour + ":00")
            time_slot_list.append(hour + ":30")
        return time_slot_list
    
    # Function to display recommended scheduling time to the user   
    def display_recommendation(self, rec_event_name):
        for e in self.time_slots:
            # print(e)
            if e[1] == rec_event_name:
                print("Ok, based on your existing calendar events, I recommend you leave for", 
                      rec_event_name, "at", e[0])
                print("""
Would you like to add this event to your calendar?""")
                try:
                    yes_no = input("(yes/no) ---> ")
                    if yes_no.lower() == "yes":
                        user_continue = True
                    elif yes_no.lower() == "no":
                        user_continue = False
                    else:
                        user_continue = None
                        
                    if user_continue == True:
                        print("""
Functionality pending.""")
                except:
                    pass
                print("""
Thank you for using PSA!""")
                break