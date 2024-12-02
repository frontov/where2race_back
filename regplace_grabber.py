from lxml import etree
from event import Event
from date_utils import russian_date_to_timestamp

import requests

req = 'https://reg.place/?q%5Bcity%5D=&q%5Bend%5D=Tue+Dec+31+2024+00%3A00%3A00+GMT%2B0300+%28Moscow+Standard+Time%29&q%5Bscope%5D=future&q%5Bsport_id%5D=any&q%5Bstart%5D=Mon+Jan+01+2024+00%3A00%3A00+GMT%2B0300+%28Moscow+Standard+Time%29&q%5Btag%5D=&q%5Btext%5D=&'
kinds = {'Бег': 'running', 'Велогонка': 'cycling', 'Лыжи': 'skiing'}


def get_count():
    headers = {'content-type': 'application/json', }
    response = requests.get(req, headers=headers)
    html = response.text
    htmlparser = etree.HTMLParser()
    tree = etree.fromstring(html, htmlparser)
    try:
        count = tree.xpath('//*[contains(@class, "pagination")]/li[position() = (last()-2)]/a/text()')
        return int(''.join(count))
    except:
        return 1


def get_events(i):
    headers = {'content-type': 'application/json', }
    response = requests.get(req + 'page=' + str(i), headers=headers)
    html = response.text
    return html


def parse_html(html):
    result = []

    htmlparser = etree.HTMLParser()
    tree = etree.fromstring(html, htmlparser)
    items = tree.xpath('//*[@class="event"]')
    for elem in items:
        name = elem.xpath('.//*[@class="name"]/a/text()')[0]
        link = "https://reg.place/" + elem.xpath('.//*[@class="name"]/a/@href')[0]
        date = elem.xpath('.//*[@class="info"]/strong/text()')[0]
        date_start, date_end = russian_date_to_timestamp(date)
        tmp = elem.xpath('.//*[@class="info"]/text()')
        region = None if len(tmp) != 3 else tmp[1].strip()
        kind = []
        raw_kind = elem.xpath('.//*[@class="info"]//text()')[-1].strip()
        array_kind = raw_kind.split(', ')
        for k in array_kind:
            kind.append(kinds.get(k, 'other'))
        # todo add distances

        event = Event(name, None, link, name, kind, None, date_start, date_end, region, None)
        result.append(event)

    return result

def parse_events():
    count = get_count()
    result = []
    for i in range(count):
        html = get_events(i+1)
        events = parse_html(html)
        result.extend(events)
    return result
