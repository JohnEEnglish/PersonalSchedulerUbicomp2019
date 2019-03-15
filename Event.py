class Event:
    """
    This class is where we will be implementing all of our event characteristics
    """

    def __init__(self, duration=-1, time="-1:00", name="", priority=0):
        self.time = time
        self.duration = duration
        self.name = name
        self.priority = priority
        self.priority_dict = {0: "Default",
                              1: "Est. Traffic Conditions",
                              2: "Weather",
                              3: "Est. Driving Time",
                              4: "Destination Popularity",
                              5: "Estimated Wait Time"}

    # Display event attributes section
    def display_event_length(self):
        print("The duration of this event is:", self.duration)

    def display_event_time(self):
        print("This event will take place at ", self.time)

    def display_event_name(self):
        print("The event name is:", self.name)

    def display_event_priority(self):
        print("The priority of this event is:", self.priority_dict[self.priority])

    # Set event attributes section
    def set_duration(self, duration=-1):
        self.duration = duration

    def set_time(self, time="-1:00"):
        self.time = time

    def set_name(self, name=""):
        self.name = name

    def set_priority(self, priority=-1):
        self.priority = priority

    # Get event attributes section
    def get_duration(self):
        return self.duration

    def get_time(self):
        return self.time

    def get_name(self):
        return self.name

    def get_priority(self):
        return self.priority

