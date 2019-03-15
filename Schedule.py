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
        current_time_index = 0
        self.events = sorted(self.events, key=lambda x: x.get_priority(), reverse=True)
        for t in self.time_slots:
            t[1] = "No event"
        for event in self.events:
            for time_slice in range(event.get_duration()):
                self.time_slots[current_time_index][1] = event.get_name()
                current_time_index += 1
#                if time_slice == event.get_duration() - 1:
#                    self.time_slots[current_time_index][1] = "Traveling"
#                    current_time_index += 1

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
    
    #TODO:  function to display recommended scheduling time to the user   
    def display_recommendation(self):
        print("The recommended scheduling time for this event is:")