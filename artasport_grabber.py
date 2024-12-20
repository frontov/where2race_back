import requests
from lxml import html

from date_utils import russian_date_to_timestamp


class Event:
    def __init__(self, name, link, description, kind, sub_kind, date_start, region):
        self.name = name
        self.link = link
        self.description = description
        self.kind = kind
        self.sub_kind = sub_kind
        self.date_start = date_start
        self.region = region


def cut_string_by_second_space(s):
    # Split the string by spaces
    parts = s.split(' ')

    # Check if there are at least two spaces
    if len(parts) < 3:
        return s  # Return the original string if there are less than two spaces

    # Join the first two parts with a space and the rest of the parts
    return ' '.join(parts[:2])


def parse(tree, kind, events):

    for event in tree.xpath('//div[@class="event_item"]'):
        name = event.xpath('.//*[@class="name"]/text()')[0]
        link = 'https://arta-sport.ru/' + event.xpath('.//a/@href')[0]
        # sub_kind = event.xpath('.//span[@class="sub-kind"]/text()')[0]
        date_start = event.xpath('.//div[@class="data"]/text()')[0]
        date_start = cut_string_by_second_space(date_start)
        date_start = russian_date_to_timestamp(date_start)
        region = event.xpath('.//div[@class="adr"]/text()')[0]

        event_obj = Event(name, link, '', kind, '', date_start[0], region)
        events.append(event_obj)


def parse_events():
    url = 'https://arta-sport.ru/predstoyaschie-meropriyatiya/'

    events = []

    response = requests.get(url + '?sortBy=1')
    tree = html.fromstring(response.content)
    parse(tree, ['skiing'], events)

    response = requests.get(url + '?sortBy=2')
    tree = html.fromstring(response.content)
    parse(tree, ['skiing'], events)

    response = requests.get(url + '?sortBy=9')
    tree = html.fromstring(response.content)
    parse(tree, ['running'], events)

    return events
