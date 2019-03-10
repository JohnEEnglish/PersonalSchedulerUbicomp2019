class Schedule:
    """
    This class will hold the schedule for a single day.
    """

    def __init__(self, event_list=list()):
        self.events = event_list
        self.time_slots = []

        def make_time_slot_name_list():
            time_slot_list = []
            for hour_int in range(24):
                if hour_int < 10:
                    hour = "0" + str(hour_int)
                else:
                    hour = str(hour_int)
                time_slot_list.append(hour + ":00")
                time_slot_list.append(hour + ":30")
            return time_slot_list

        time_slot_name_list = make_time_slot_name_list()
        for slot in time_slot_name_list:
            self.time_slots.append([slot, "No Event"])

    def update_schedule(self):
        current_time_index = 0
        for event in self.events:
            for time_slice in range(event.duration):
                self.time_slots[current_time_index][1] = event.get_name()
                self.time_slots[current_time_index][1] = "Traveling"
                current_time_index += 2

    def display_schedule(self):
        for slot in self.time_slots:
            print("At time::", slot[0], slot[1], "is scheduled.")

    def add_event(self, event):
        self.events.append(event)
        self.update_schedule()
