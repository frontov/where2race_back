import russialoppet_grabber
import russiarunning_grabber
import regplace_grabber
import orgeo_grabber
from date_utils import timestamp_to_datetime
import db


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
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

    # bike = db.db.search(db.events.kind.any(['cycling']))

    # print(len(bike))
    # for event in bike:
    #     print(event)

    # all = sorted(db.db.all(), key=lambda k: k['date_start'])
    # for event in all:
    #     print( event['kind'], timestamp_to_datetime(event['date_start']), event['link'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

''' there is tinydb with table 'events' object like this {
      "name": "name",
      "link": "link",
      "kind": [
        "kind"
      ],
      "sub_kind": "",
      "date_start": 1749607200,
      "date_finish": 0,
      "region": "region"
    }
    write a telegram bot using python and aiogram3 which will be work with that db and send to user events with filter.
    filter by kind, date_start. 
    bot must be with InlineKeyboard
          
          
'''
