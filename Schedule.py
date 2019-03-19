class Schedule:
    """
    This class will hold the schedule for a single day.
    """

    def __init__(self, event_list=[]):
        self.events = event_list
        self.time_slots = []
        self.morning_buffer = 6 # No events will be scheduled prior to this time (6am)
        self.evening_buffer = 22 # No events will be scheduled after this time

        time_slot_name_list = self.make_time_slot_name_list()
        for slot in time_slot_name_list:
            self.time_slots.append([slot, "No Event", 0])

    def update_schedule(self):
        self.events = sorted(self.events, key=lambda x: x.get_priority(), reverse=True)
        for t in self.time_slots:
            t[1] = "No event"
        # self.time_slots = self.make_schedule_from_events()
        self.time_slots = self.make_schedule_from_events_static()

    def make_schedule_from_events(self):
        from copy import deepcopy
        current_time_index = 0
        temp_slots = deepcopy(self.time_slots)

        for event in self.events:
#             if event.get_priority() == 5:
#                 from random import choice
#                 wait_times = [0] * 9 + [1] * 3 + [2] * 1
#                 event_wait_time = choice(wait_times)
#                 # current_time_index = self.wait_time_offset(time_slots=temp_slots,
#                 #                                            wait_time=event_wait_time,
#                 #                                            c_t_index=current_time_index)

            for time_slice in range(event.get_duration()):
                temp_slots[current_time_index][1] = event.get_name()
                current_time_index += 1
                if time_slice == event.get_duration() - 1:
                    current_time_index = self.travel_offset(time_slots=temp_slots,
                                                            travel_time=1,
                                                            c_t_index=current_time_index)

        return temp_slots

    def make_schedule_from_events_static(self):
        """
        This can be thought to run with the following psudocode:
        for every event in a prioritized event list:
            for every time slot that both within our schedule's time and the operating hours of our event's venue:
                check to see if there is space to fit the event starting at the current time slot:
                    if there is add the event
                    if there isn't move to the next time slot
        :return:
        """
        from random import choice
        temp_slot_name_list = self.make_time_slot_name_list_no_buffers()
        temp_slots = []
        rand_pool = [0]*3 + [1]*3 + [2]*3
        for slot in temp_slot_name_list:
            temp_slots.append([slot, "No event", choice(rand_pool)])
        travel_time = 0
        for event in self.events:
            for start_time in range(max([self.morning_buffer*2, event.get_hours_of_operation()[0]*2]),
                                    min([self.evening_buffer*2 - 1, event.get_hours_of_operation()[1]*2 - 1])):
                valid_time = True
                try:
                    if event.static:
                        for current_time in range(event.get_duration() + travel_time):
                            # print("current_time:", current_time)
                            if temp_slots[start_time + current_time][1] != 'No event':
                                valid_time = False
                                # print("temp_slot attributes:", temp_slots[start_time + current_time])
                                print("ERROR MULTIPLE STATIC EVENTS BEING SCHEDULED ON TOP OF ONE ANOTHER")
                    else:
                        for current_time in range(event.get_duration() + travel_time):
                            # print("current_time:", current_time)
                            if temp_slots[start_time + current_time][1] != 'No event' \
                                    or temp_slots[start_time + current_time][2] > 1:
                                valid_time = False
                                # print("temp_slot attributes:", temp_slots[start_time + current_time])
                except:
                    print("""DUE TO THE ESTIMATED STATE OF EXTERNAL FACTORS TODAY, SCHEDULING THIS EVENT IS NOT RECOMMENDED.
                          """)
                    break
                if valid_time:
                    assert temp_slots[start_time + current_time][1] == 'No event', "ERROR"
                    current_time_index = start_time
                    # if event.get_priority() == 5:
                        # wait_times = [0] * 9 + [1] * 3 + [2] * 1
                        # event_wait_time = choice(wait_times)
                        # current_time_index = self.wait_time_offset(time_slots=temp_slots,
                        #                                            wait_time=event_wait_time,
                        #                                            c_t_index=current_time_index)

                    for time_slice in range(event.get_duration()):
                        temp_slots[current_time_index][1] = event.get_name()
                        current_time_index += 1
                        if time_slice == event.get_duration() - 1:
                            current_time_index = self.travel_offset(time_slots=temp_slots,
                                                                    travel_time=0,
                                                                    c_t_index=current_time_index)
                    break
            # print("Event Processed Successfully")

        return temp_slots

    @staticmethod
    def travel_offset(time_slots=[], travel_time=1, c_t_index=0):
        for x in range(travel_time):
            time_slots[c_t_index][1] = "Traveling"
            c_t_index += 1

        return c_t_index

    @staticmethod
    def wait_time_offset(time_slots=[], wait_time=1, c_t_index=0):
        for x in range(wait_time):
            time_slots[c_t_index][1] = "Waiting"
            c_t_index += 1

        return c_t_index

    def display_schedule(self):
        """
        This prints out the schedule
        :return:
        """
        for slot in self.time_slots[self.morning_buffer * 2: self.evening_buffer*2-1]:
            print("At time:", slot[0], slot[1], "is scheduled.")
#            print("")

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

    @staticmethod
    def make_time_slot_name_list_no_buffers():
        time_slot_list = []
        for hour_int in range(0, 23, 1):
            if hour_int < 10:
                hour = "0" + str(hour_int)
            else:
                hour = str(hour_int)
            time_slot_list.append(hour + ":00")
            time_slot_list.append(hour + ":30")
        return time_slot_list
    
    # Function to display recommended scheduling time to the user   
    def display_rec(self, rec_event_name):
        for e in self.time_slots:
            # print(e)
            if e[1] == rec_event_name:
                print("Ok, based on [external factors], I recommend you leave for", 
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