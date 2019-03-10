class Schedule:
    """
    This class will hold the schedule for a single day.
    """

    def __init__(self, event_list=[]):
        self.events = event_list

    def display_schedule(self):
        for event in self.events:
            event.display_event_length()

    def add_event(self, event):
        self.events.append(event)