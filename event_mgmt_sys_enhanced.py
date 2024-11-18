'''
Extend an existing Event class by adding a feature to keep track 
of the number of participants. Implement a method add_participant 
that increases the count and a method get_participant_count to 
retrieve the current count.

- Code Example: Basic Event class without participant tracking.

    class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date

'''

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []

    def add_participant(self, name):
        if name in self.participants:
            print(f"{name} is already a participant in the event.")
        else:
            self.participants.append(name)
            print(f"{name} has been added.")
    
    def get_participant_count(self):
        return len(self.participants)
    
event = Event("Prom", "12/12/24")
event.add_participant("Den")
event.add_participant("Alice")
event.add_participant("Kleng")
event.add_participant("Ava")

print(f"Current participants: {event.get_participant_count()}")