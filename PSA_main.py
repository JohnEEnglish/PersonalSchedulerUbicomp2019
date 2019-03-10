from Event import Event
from Schedule import Schedule


def main_one():
    event_one = Event(1, name="Tennis")
    event_two = Event(2, name="Scuba Diving")
    schedule_main_one = Schedule()
    schedule_main_one.add_event(event_one)
    schedule_main_one.add_event(event_two)
    schedule_main_one.display_schedule()


if __name__ == "__main__":
    main_one()
