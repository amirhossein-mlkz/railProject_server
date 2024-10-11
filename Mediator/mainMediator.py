
class Event:

    def __init__(self, name, func, priority) -> None:
        self.func = func
        self.name = name
        self.priority = priority
    def __str__(self) -> str:
        return f"event_name: {self.name} - func:{self.func}"
    

class Filter:

    def __init__(self, name, func, priority) -> None:
        self.func = func
        self.name = name
        self.priority = priority
    def __str__(self) -> str:
        return f"Filter name: {self.name} - func:{self.func}"
    


class Mediator:
    _instance = None  # Class variable to hold the singleton instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        # Ensure the __init__ method only runs once
        if not hasattr(self, 'initialized'):
            self.events:dict[str, list[Event]] = {}
            self.filters:dict[str, list[Event]] = {}
            self.initialized = True

    def register_events(self, event_name:str):
        if event_name not in self.events:
            self.events[event_name] = []
        else:
            print(f'Event {event_name} already exists')

    def add_event_listener(self, event_name, priority, func):
        assert event_name in self.events, f"add listener for {event_name} but not exist"
        e = Event(event_name, func, priority)
        self.events[event_name].append(e)
        self.events[event_name].sort( key=lambda x:x.priority)


    def start_event(self, event_name:str, args, kwargs={}):
        assert event_name in self.events, f"start event for {event_name} but not exist"

        for e in self.events[event_name]:
            e.func(*args, **kwargs)



    def register_filter(self, filter_name:str):
        if filter_name not in self.events:
            self.events[filter_name] = []
        else:
            print(f'Filter {filter_name} already exists')

    def add_filter_listener(self, filter_name, priority, func):
        assert filter_name in self.events, f"add listener for {filter_name} but not exist"
        f = Filter(filter_name, func, priority)
        self.filters[filter_name].append(f)
        self.filters[filter_name].sort( key=lambda x:x.priority)


    def start_filters(self, filter_name:str, args, kwargs={}):
        assert filter_name in self.events, f"start Filter for {filter_name} but not exist"

        for e in self.filters[filter_name]:
            args, kwargs = e.func(*args, **kwargs)

