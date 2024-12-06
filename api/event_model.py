from datetime import datetime


def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%d.%m.%y")


class EventModel:
    name = None
    link = None
    description = None
    kind = None
    kind_rus = None
    sub_kind = None
    date = None
    timestamp_date = None
    address = None

    def __init__(self, event):
        self.name = event['name']
        self.link = event['link']
        self.description = event['description']
        self.kind = ", ".join(event['kind'])
        self.kind_rus = ", ".join(event.get('kind_rus', ''))
        self.sub_kind = event['sub_kind']
        self.date = timestamp_to_datetime(event['date_start'])
        self.timestamp_date = int(event['date_start'])
        self.address = event['region']
