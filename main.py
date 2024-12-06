from datetime import datetime

import artasport_grabber
import russialoppet_grabber
import russiarunning_grabber
import regplace_grabber
import orgeo_grabber
import db

count = 0
now = round(datetime.now().timestamp())


def upsert_events(e):
    global count
    for event in e:
        db.upsert_event(event)
        if (now < event.date_start):
            count = count + 1


if __name__ == '__main__':
    events = regplace_grabber.parse_events()
    upsert_events(events)

    events = russialoppet_grabber.parse_events()
    upsert_events(events)


    events = russiarunning_grabber.parse_events()
    upsert_events(events)


    events = orgeo_grabber.parse_events()
    upsert_events(events)

    events = artasport_grabber.parse_events()
    upsert_events(events)

    print(count)
