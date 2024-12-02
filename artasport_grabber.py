import requests
from lxml import html


class Event:
    def __init__(self, name, link, description, kind, sub_kind, date_start, region):
        self.name = name
        self.link = link
        self.description = description
        self.kind = kind
        self.sub_kind = sub_kind
        self.date_start = date_start
        self.region = region


def parse_events(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)

    events = []
    for event in tree.xpath('//div[@class="event_item"]'):
        name = event.xpath('.//*[@class="name"]/text()')[0]
        link = event.xpath('.//a/@href')[0]
        kind = event.xpath('.//span[@class="kind"]/text()')
        sub_kind = event.xpath('.//span[@class="sub-kind"]/text()')[0]
        date_start = event.xpath('.//span[@class="date-start"]/text()')[0]
        region = event.xpath('.//span[@class="region"]/text()')[0]

        event_obj = Event(name, link, '', kind, sub_kind, date_start, region)
        events.append(event_obj)

    return events


url = 'https://arta-sport.ru/predstoyaschie-meropriyatiya/'
events = parse_events(url)

for event in events:
    print(f"Name: {event.name}")
    print(f"Link: {event.link}")
    print(f"Description: {event.description}")
    print(f"Kind: {', '.join(event.kind)}")
    print(f"Sub-kind: {event.sub_kind}")
    print(f"Date Start: {event.date_start}")
    print(f"Region: {event.region}")
    print()
