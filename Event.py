class Event:
    """
    This class is where we will be implementing all of our event characteristics
    """

    def __init__(self, duration=1, time="00:00", name=""):
        self.time = time
        self.duration = duration
        self.name = name

    def display_event_length(self):
        print("The duration of this event is:", self.duration)

    def display_event_time(self):
        print("This event will take place at ", self.time)

    def display_event_name(self):
        print("The event name is:", self.name)

    def get_duration(self):
        return self.duration

    def get_time(self):
        return self.time

    def get_name(self):
        return self.name

