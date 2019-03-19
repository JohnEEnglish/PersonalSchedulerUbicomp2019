class Event:
    """
    This class is where we will be implementing all of our event characteristics
    """

    def __init__(self, duration=-1, time="-1:00", name="", location = "",
                 priority=0, hours_of_operation=(0, 24), static_flag=False):
        self.time = time
        self.duration = duration
        self.name = name
        self.location = location
        self.priority = priority
        self.static = static_flag
        self.hours_of_operation = hours_of_operation
        self.priority_dict = {0: "Default",
                              1: "Traffic Conditions",
                              2: "Weather",
                              3: "Crowd Level",
                              4: "Wait Time"}

    # Display event attributes section
    def display_event_length(self):
        print("The duration of this event is:", self.duration)

    def display_event_time(self):
        print("This event will take place at ", self.time)

    def display_event_name(self):
        print("The event name is:", self.name)
        
    def display_event_loc(self):
        print("The event name is:", self.location)        

    def display_event_priority(self):
        print("The priority of this event is:", self.priority_dict[self.priority])

    def display_event_hours_of_operation(self):
        print("The hours of availability operation for this venue are:", self.operation)

    def display_static(self):
        print("Is the event static:", self.static)

    # Set event attributes section
    def set_duration(self, duration=-1):
        self.duration = duration

    def set_time(self, time="-1:00"):
        self.time = time

    def set_name(self, name=""):
        self.name = name
        
    def set_location(self, location=""):
        self.location = location        

    def set_priority(self, priority=-1):
        self.priority = priority

    def set_hours_of_operation(self, hours_of_operation=(0, 24)):
        self.hours_of_operation = hours_of_operation

    def set_static(self, static_flag=False):
        self.hours_of_operation = static_flag

    # Get event attributes section
    def get_duration(self):
        return self.duration

    def get_time(self):
        return self.time

    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.location    

    def get_priority(self):
        return self.priority

    def get_hours_of_operation(self):
        return self.hours_of_operation

    def get_static(self):
        return self.static
