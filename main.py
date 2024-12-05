import artasport_grabber
import russialoppet_grabber
import russiarunning_grabber
import regplace_grabber
import orgeo_grabber
import db

if __name__ == '__main__':
    events = regplace_grabber.parse_events()
    for event in events:
        db.upsert_event(event)

    events = russialoppet_grabber.parse_events()
    for event in events:
        db.upsert_event(event)

    events = russiarunning_grabber.parse_events()
    for event in events:
        db.upsert_event(event)
    events = orgeo_grabber.parse_events()
    for event in events:
        db.upsert_event(event)
    events = artasport_grabber.parse_events()
    for event in events:
        db.upsert_event(event)
