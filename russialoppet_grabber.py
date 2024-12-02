from lxml import etree
from event import Event
from date_utils import date_to_timestamp

import requests


def get_events():
    headers = {'content-type': 'application/json', }
    response = requests.get('https://russialoppet.ru/events/2025/', headers=headers)
    html = response.text
    return html


def parse_events():
    result = []
    html = get_events()

    htmlparser = etree.HTMLParser()
    tree = etree.fromstring(html, htmlparser)
    items = tree.xpath('//tbody/*[@class="item"]')
    for elem in items:
        name = elem.xpath('.//td/a/text()')[0]
        link = elem.xpath('.//td/a/@href')[0]
        date = date_to_timestamp(elem.xpath('.//*[@class="date"]/text()')[0])
        region = ',     '.join(elem.xpath('.//span[not(@class)]//text()'))
        # todo add distances
        subtype = elem.xpath('.//b[2]/text()')

        event = Event(name=name, date_start=date, date_finish=date, region=region, sub_kind=subtype, kind=['skiing'],
                      link="https://russialoppet.ru" + link, slug=None, description=None, distances=None)

        result.append(event)

    return result
