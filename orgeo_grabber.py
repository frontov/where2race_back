# https://orgeo.ru/event/index/type/cycling?search=
from lxml import etree
from event import Event
from date_utils import dates_to_timestamp

import requests

req = 'https://orgeo.ru/event/index/type/'

kinds = {'athletics': 'running', 'cycling': 'cycling', 'skiing': 'skiing'}


def get_events(kind):
    headers = {'content-type': 'application/json', }
    response = requests.get(req + kind, headers=headers)
    html = response.text
    return html


def parse_html(html):
    result = []

    htmlparser = etree.HTMLParser()
    tree = etree.fromstring(html, htmlparser)
    items = tree.xpath('//table[contains(@class, "tableEvents")]/tbody/tr')
    for elem in items:
        name = elem.xpath('.//table[@class="event_view_block"]//a/span/text()')[1]
        link = "https://orgeo.ru" + elem.xpath('.//a/@href')[0]
        date = elem.xpath('.//b/text()')[0]
        date_start, date_end = dates_to_timestamp(date)
        region = elem.xpath('.//*[@class="event-place"]/text()')[0]
        # kind = ['other']
        # todo add distances

        event = Event(name, None, link, name, None, None, date_start, date_end, region, None)
        result.append(event)

    return result


def parse_events():
    result = []
    for kind in list(kinds.keys()):
        html = get_events(kind)
        events = parse_html(html)
        for event in events:
            event.set_kind(kinds[kind].split())
        result.extend(events)
    return result
