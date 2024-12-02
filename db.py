import tinydb

from event import Event

db = tinydb.TinyDB('db.json')
events = tinydb.Query()


def upsert_event(event):
    condition = events.date_start == event.date_start and events.name == event.name
    print(id)
    is_exist = db.search(condition)

    if is_exist:
        # Update the existing user
        db.update(event.__dict__, condition)
        print(f"Updated event {event}")
    else:
        # Insert a new user
        db.insert(event.__dict__)
        print(f"Inserted event {event}")
